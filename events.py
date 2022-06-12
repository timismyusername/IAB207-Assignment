from datetime import date
import re
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
import flask_login
from .models import Event, Comment
from .forms import EventForm, CommentForm
from . import db
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('/<id>')
def show(id):
    event = Event.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('event_details.html', event=event, form=cform)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.is_submitted():
    db_file_path=check_upload_file(form)
    event = Event(name=form.name.data, 
    email=form.email.data, 
    date=form.date.data, 
    time=form.time.data, 
    location=form.location.data, 
    organiser=form.organiser.data, 
    status=form.status.data, 
    artists=form.artists.data, 
    genre=form.genre.data, 
    description= form.description.data, 
    price=form.price.data, 
    image=db_file_path)
    print("The event name is:", form.name.data)
    # add the object to the db session
    db.session.add(event)
    db.session.commit()
    print('Successfully created new event', 'success')
    #redirect when form is valid
    return redirect(url_for('event.create'))
  return render_template('creation.html', form=form)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/img',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/img/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<event>', methods = ['GET', 'POST'])  
@login_required
def comment(event):  
    form = CommentForm()  
    #get the event object associated to the page and the comment
    event_obj = Event.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data, event_id=event_obj.id, user= current_user) 
      print("The following comment has been posted:", form.text.data)
      
      #here the back-referencing works - comment.event is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to event.show
    return redirect(url_for('event.show', id=event)) 
    
