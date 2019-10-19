from app import db


class Face(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    face_id = db.Column(db.Text, nullable=False)

    def __init__(self, user_id, face_id):
        self.user_id = user_id
        self.face_id = face_id