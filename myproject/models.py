from flaskblog import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    age = db.Column(db.String(3), nullable=True)
    gender = db.Column(db.String(6), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    def __init__(self,username=None, email=None, password=None, age=None, gender=None, phone=None, address=None):
        self.username= username
        self.email = email
        self.password
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.age}', '{self.gender}','{self.phone}', '{self.address}')"
