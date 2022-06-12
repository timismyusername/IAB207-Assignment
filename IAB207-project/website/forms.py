
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from wtforms import DateField, TimeField, FloatField, SelectField
from flask_wtf.file import FileRequired, FileField, FileAllowed
ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg', 'jpeg'}


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired("Create a user name"), Length(min=5, max=20)])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    phone_number = IntegerField("Contact number", validators=[InputRequired("Please enter a valid phone number")])
    address = StringField("Address", validators=[InputRequired(), Length(min=5, max=30)])
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

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
