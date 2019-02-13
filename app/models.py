from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(8))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25))
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

class Login:
    login=[]
    def __init__(self,username,password):
        self.username = username
        self.password = password
        1
class Register:
    register=[]
    def __init__(self,username,email,password,confirmpassword):
        self.username = username
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword

class Pickuplines:
    pitch=[]
    def __init__(self,pickupline,author):
        self.pickupline = pickupline
        self.author = author

class Promotion:
    promotion=[]
    def __init__(self,promo,author):
        self.promo = promo
        self.author = author

class Product:
    product=[]
    def __init__(self,products,author):
        self.products = products
        self.author = author

class Interview:
    interview=[]
    def __init__(self,interviews,author):
        self.interviews = interviews
        seld.author = author

class Pitch(db.Model):
    __tablename__ = 'pitches'


    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(), index=True)
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"
