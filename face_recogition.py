from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from msrest.authentication import CognitiveServicesCredentials
import io
import uuid
import os
from datetime import datetime
import time
import sys
from models import User
from app import db


def set_environ_variables():
    env_file = '.env'
    with open(env_file) as envfile:
        for line in envfile:
            data = line.split('=')
            os.environ[data[0].strip()] = data[1].strip()

set_environ_variables()

PERSON_GROUP_ID = 'all-people'

face_api_key = os.environ.get('FACE_SUBSCRIPTION_KEY', None)
assert face_api_key
face_api_endpoint = os.environ.get('FACE_ENDPOINT', None)
assert face_api_endpoint

credentials = CognitiveServicesCredentials(face_api_key)
face_client = FaceClient(face_api_endpoint, credentials=credentials)


def get_training_status():
    while (True):
        training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
        print("Training status: {}.".format(training_status.status))
        print()
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            sys.exit('Training the person group has failed.')
        time.sleep(5)


def register_face(images, person_name):
    person = face_client.person_group_person.create(PERSON_GROUP_ID, person_name)
    user = User.get_by_username(person_name)
    user.person_id = person.person_id
    db.session.add(user)
    db.session.commit()
    for image in images:
        image = io.BytesIO(image)
        face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, person.person_id, image)
    print('New person added: ', person_name)
    print('Starting Training.')
    face_client.person_group.train(PERSON_GROUP_ID)
    get_training_status()


def find_person(image):
    image = io.BytesIO(image)
    faces = face_client.face.detect_with_stream(image)
    face_ids = [face.face_id for face in faces]
    results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
    if not results:
        return None
    else:
        for result in results:
            # Find the top candidate for each face
            candidates = sorted(result.candidates, key=lambda c: c.confidence, reverse=True)
            # Was anyone recognized?
            if len(candidates) > 0:
                # Get just the top candidate
                top_candidate = candidates[0]
                # See who the person is
                person = face_client.person_group_person.get(PERSON_GROUP_ID, top_candidate.person_id)
                return str(person.name)
            return None

#face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)