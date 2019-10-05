from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,EqualTo, Email



class RegistrationForm(FlaskForm):
	username=StringField("Your Username Here",validators=[DataRequired(),Length(min=5)])
	email=StringField("Your Email Here",validators=[DataRequired(),Email()])
	password=PasswordField("Your Password Here",validators=[DataRequired()])
	confirm_password=PasswordField("Confirm your password again",validators=[DataRequired(),\
		EqualTo('password')])
	submit=SubmitField('Register')


class LoginForm(FlaskForm):
	
	email=StringField("Your Email Here",validators=[DataRequired(),Email()])
	password=PasswordField("Your Password Here",validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')