from flaskblog import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    age = db.Column(db.String(3), nullable=True)
    gender = db.Column(db.String(6), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    height = db.Column(db.String(3), nullable = False)
    weight = db.Column(db.String(20), nullable = False)
    bloodgroup = db.Column(db.String(7), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.age}', '{self.gender}','{self.phone}', '{self.address}')"
