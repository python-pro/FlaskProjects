from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, ValidationError
from wtforms.validators import InputRequired, Length
from flask_bootstrap import Bootstrap
import secrets


"""
Inline validation is added 


And it functions in comnination with app3index.html doc.

"""

app=Flask(__name__)
app.config['SECRET_KEY']=secrets.token_hex(16)
# bootstrap=Bootstrap(app)


class LoginForm(FlaskForm):
	
	username=StringField('Your username',validators=[InputRequired('A username is required'),\
		Length(min=5,max=12, message='Between 5 and 12')])
	
	password=PasswordField('Your password',validators=[InputRequired('Put the password')])

	def validate_username(form,field):
		if field.data!="AbdulMalik":
			raise ValidationError("You are not signed up bro")


@app.route('/', methods=['GET','POST'])
def index():

	form=LoginForm()

	if form.validate_on_submit():
	
		return "<h1>Successfully Submitted<h1>"

	return render_template('app3index.html', form=form)


if __name__=='__main__':
	app.run(debug=True)



