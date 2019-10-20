from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    balance = db.Column(db.Integer)
    password = db.Column(db.Text)
    faces = db.relationship('Face', backref='user', lazy=True)
    checks = db.relationship('Check', backref='user', lazy=True)
    person_id = db.Column(db.Text)

    def __init__(self, username, password='password'):
        self.username = username
        self.password = password
        self.balance = 100
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_by_user_id(id):
        return User.query.filter_by(id=id).first()
    
    @staticmethod
    def get_by_person_id(person_id):
        return User.query.filter_by(person_id=person_id).first()

class Face(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    face_id = db.Column(db.Text, nullable=False)

    def __init__(self, user_id, face_id):
        self.user_id = user_id
        self.face_id = face_id


class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    check_in_time = db.Column(db.DateTime)
    check_in_station = db.Column(db.UnicodeText)
    check_out_time = db.Column(db.DateTime)
    check_out_station = db.Column(db.UnicodeText)
    cost = db.Column(db.Integer)

    def __init__(self, user_id, check_in_time, check_in_station, check_out_time=None, check_out_station=None, cost=None):
        self.user_id = user_id
        self.check_in_station = check_in_station
        self.check_in_time = check_in_time
        self.check_out_station = check_out_station
        self.check_out_time = check_out_time
        self.cost = cost
    
    def on_checkout(self, check_out_station, check_out_time, cost):
        self.check_out_station = check_out_station
        self.check_out_time = check_out_time
        self.cost = cost