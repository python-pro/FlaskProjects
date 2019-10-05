from flask import Flask,render_template
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired, Length
from collections import namedtuple
import secrets


"""
Recaptcha functionality is added, 
and just for prevention purposes made changes in configuration to prevent poppin up of recaptcha.

And it functions in comnination of app2form.html doc.

"""

app=Flask(__name__)
app.config['SECRET_KEY']=secrets.token_hex(16)

app.config['RECAPTCHA_PUBLIC_KEY']='6LdsxbcUAAAAAE3uGyzNrorw4OrpuDRK-x643FzQ'
app.config['RECAPTCHA_PRIVATE_KEY']='6LdsxbcUAAAAAEcgGWu4UJ3J6Vnx0rI4fMg8WLBI'
app.config['TESTING']=True


class LoginForm(FlaskForm):
	
	username=StringField('Your username',validators=[InputRequired('A username is required'),\
		Length(min=5,max=12, message='Between 5 and 12')])
	
	password=PasswordField('Your password',validators=[InputRequired('Put the password')])
	recaptcha=RecaptchaField()
	


@app.route('/app2form', methods=['GET','POST'])
def form():


	form=LoginForm()


	if form.validate_on_submit():
		

		return "<h1>Blah blah blah <h1>"

	return render_template('app2form.html', form=form)


if __name__=='__main__':
	app.run(debug=True)



