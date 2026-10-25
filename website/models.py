from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#database mdodel is just layout for what the infos must satisfy
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #associating information with user w/foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #wUser class uses proper, the sql actually recieves it as lower (user)

class User(db.Model, UserMixin): #UserMixin is just because we inherit from flask_login
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #String(charlimit), unique=cannot be the same as others'
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #yeah we dont need the .id

