from flask import Flask,render_template
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,PasswordField,IntegerField,BooleanField,Form, FormField,FieldList
from wtforms.validators import InputRequired, Length, AnyOf, Email
import secrets,os
from collections import namedtuple


app=Flask(__name__)
app.config['SECRET_KEY']=secrets.token_hex(16)
app.config['WTF_CSRF_ENABLED']=True
app.config['WTF_CSRF_SECRET_KEY']=os.urandom(16)
app.config['WTF_CSRF_TIME_LIMIT']=25
app.config['RECAPTCHA_PUBLIC_KEY']='6LdsxbcUAAAAAE3uGyzNrorw4OrpuDRK-x643FzQ'
app.config['RECAPTCHA_PRIVATE_KEY']='6LdsxbcUAAAAAEcgGWu4UJ3J6Vnx0rI4fMg8WLBI'

class PhoneForm(Form):
	country_code=IntegerField('Country_Code')
	area_code=IntegerField('Area_Code')
	number=StringField('Number')

class YearForm(Form):
	year=IntegerField('Year')
	total=IntegerField("Total")

class LoginForm(FlaskForm):
	recaptcha=RecaptchaField()
	username=StringField('Your username',validators=[InputRequired('A username is required'),\
		Length(min=5,max=12, message='Between 5 and 12')])
	email=StringField('Your email',validators=[Email('Please use valid email')])
	password=PasswordField('Your password',validators=[InputRequired('Put the password')])
	age=IntegerField('Your age goes here :)')
	boolean=BooleanField('Click for YES')
	home_phone=FormField(PhoneForm)
	mobile_phone=FormField(PhoneForm)
	years=FieldList(FormField(YearForm))



class User:
	def __init__(self,username,email,age,boolean):
		self.username=username
		self.email=email
		self.age=age
		self.boolean=boolean



@app.route('/', methods=['GET','POST'])
def index():
	myuser=User('AbdulMalik','abdumalik88@gmail.com',31,True)

	group=namedtuple("Group",['year','total'])
	g1=group(2006,1912)
	g2=group(2008,1512)
	g3=group(2019,2064)

	years={'years':[g1,g2,g3]}


	form=LoginForm(obj=myuser,data=years)
	del form.mobile_phone

	if form.validate_on_submit():
		# return '<h1>Username: {}<br>MobileNumber: {} {} {}</h1>'.format(form.username.data, \
		# 	form.mobile_phone.country_code.data,form.mobile_phone.area_code.data,form.mobile_phone.number.data)
		output ='<h1>'

		for f in form.years:
			output+='Year: {}<br>'.format(f.year.data)

			output+='Total: {}<br>'.format(f.total.data)
		output+='</h1>'

		return output

	return render_template('index.html', form=form)


@app.route('/dynamic', methods=['GET','POST'])
def dynamic():
	class DynamicForm(FlaskForm):
		pass

	DynamicForm.name=StringField('Your name')
	names=['f_name','l_name','m_name']

	for name in names:
		setattr(DynamicForm,name,StringField(name))

	form=DynamicForm()

	if form.validate_on_submit():
		return "<h1>The form has been submitted.<br>Name is {}</h1>".format(form.name.data)
	return render_template('dynamic.html',form=form,names=names)



if __name__=='__main__':
	app.run(debug=True)



