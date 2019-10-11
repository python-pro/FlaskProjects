from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length,EqualTo, Email,ValidationError
from flaskblog.models import User



class RegistrationForm(FlaskForm):
	username=StringField("Your Username Here",validators=[DataRequired(),Length(min=5)])
	email=StringField("Your Email Here",validators=[DataRequired(),Email()])
	password=PasswordField("Your Password Here",validators=[DataRequired()])
	confirm_password=PasswordField("Confirm your password again",validators=[DataRequired(),\
		EqualTo('password')])
	submit=SubmitField('Register')


	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("This username has been taken. Please choose another one")

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("This email has been taken. Please choose another one")



class LoginForm(FlaskForm):
	
	email=StringField("Your Email Here",validators=[DataRequired(),Email()])
	password=PasswordField("Your Password Here",validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')



class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
                        validators=[DataRequired(), Email()])
	picture=FileField('Update Profile Picture', validators=[FileAllowed(['jpeg','png','jpg'])])
    
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a different one.')




class PostForm(FlaskForm):
	
	title=StringField("Title",validators=[DataRequired()])
	content=TextAreaField("Intended Content Here",validators=[DataRequired()])
	submit=SubmitField("Post")
	