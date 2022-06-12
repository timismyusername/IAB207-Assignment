
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from wtforms import DateField, TimeField, FloatField, SelectField
from flask_wtf.file import FileRequired, FileField, FileAllowed
ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg', 'jpeg'}




#Create new event
class EventForm(FlaskForm):
  name = StringField('Event Name', validators=[InputRequired()])
  email = StringField('Email', validators=[InputRequired()])
  date = DateField('Event Date', format='%Y-%m-%d', validators=[InputRequired()])
  time = TimeField('Event Time', format='%H:%M', validators=[InputRequired()])
  location = StringField('Event Location', validators=[InputRequired()])
  organiser = StringField('Organiser Name', validators=[InputRequired()])
  status = SelectField('Status', choices=[('Upcoming', 'Upcoming'), ('Booked', 'Booked'), ('Cancelled', 'Canclled'), ('Inactive', 'Inactive')])
  artists = StringField('Artists', validators=[InputRequired()])
  genre = StringField('Genre', validators=[InputRequired()])
  description = TextAreaField('Description', validators=[InputRequired()])
  price=FloatField('Price', validators=[InputRequired()])
  image = FileField('Event Image', validators=[FileRequired(), FileAllowed(ALLOWED_FILE, message='Only supports jpg,png,JPG,PNG')])
  submit = SubmitField("Create")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')