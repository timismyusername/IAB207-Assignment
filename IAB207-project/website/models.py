from . import db
from datetime import datetime
from flask_login import UserMixin



class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    date = db.Column(db.Date,nullable=False)
    time = db.Column(db.Time,nullable=False)
    location = db.Column(db.String(100),nullable=False)
    organiser = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    status = db.Column(db.String(100),nullable=False)
    artists = db.Column(db.String(200),nullable=False)
    genre = db.Column(db.String(20))
    description = db.Column(db.String(200),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    image = db.Column(db.String(400))
    # Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='events')


    def __repr__(self): 
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))


    def __repr__(self):
        return "<Comment: {}>".format(self.text)
