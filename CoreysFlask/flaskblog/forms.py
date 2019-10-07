from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
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