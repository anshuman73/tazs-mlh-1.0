from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)
    balance = db.Column(db.Integer)
    password = db.Column(db.Text)

    def __init__(self, user_name, password='password'):
        self.user_name = user_name
        self.password = password
        self.balance = 100
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username)


class Face(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    face_id = db.Column(db.Text, nullable=False)

    def __init__(self, user_id, face_id):
        self.user_id = user_id
        self.face_id = face_id