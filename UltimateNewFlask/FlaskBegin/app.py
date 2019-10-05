
from flask import Flask, jsonify, request, url_for,\
 redirect, session, render_template, g
import sqlite3


app=Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']='2e50e1382f1e0ce98b5fc5e7b05c4295fa38b925'

def connect_db():
	sql=sqlite3.connect('/home/ffulan/Dev/Flask/UltimateFlask/FlaskApp/data.db')
	sql.row_factory=sqlite3.Row
	return sql

def get_db():
	if not hasattr(g,'sqlite3'):
		g.sqlite_db=connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g,'sqlite_db'):
		g.sqlite_db.close()

@app.route('/')
def index():
	session.pop('name',None)
	return '<h1>Welcome to Ultimate Flask</h1>'


	
@app.route('/home', methods=['POST',"GET"], defaults={'name':'AbdlMalik'})
@app.route('/home/<name>', methods=['POST',"GET"])
def home(name):
	session['name']=name
	db=get_db()
	cur=db.execute('select id, name,location from users')
	results=cur.fetchall()
	return render_template('home.html',name=name,display=True,\
		myList=['Arabic','English','Russian','Persian'],\
		activityType=[{"task":'reading'},{"task":'writing'},\
		{"task":'speaking'}],results=results)
	

@app.route('/json')
def json():
	if 'name' in session:
		name=session['name']
	else:
		name="NotInSession"
	return jsonify({'key':'value', "key2":[1,2,3,4,5,6], "name":name})


@app.route('/query')
def query():
	name=request.args.get('name')
	location=request.args.get('location')
	return '<h1>Hello {}. So you are from {}. Welcome to Ultimate\
	 Flask</h1>'.format(name, location)

@app.route('/theform', methods=['POST','GET'])
def theform():
	if request.method=='GET':
		return render_template('form.html')

	else:
		name=request.form['name']
		location=request.form['loc']

		db=get_db()
		db.execute('insert into users (name, location) values (?,?)',\
			[name,location])
		db.commit()

		# loc=request.form['loc']
		# return '<h1>Hello {} from {}. \
		#You have successfully submitted the form.</h1>'.format(name,loc)
		return redirect(url_for('home',name=name))



@app.route('/processjson', methods=['POST'])
def processjson():
	data=request.get_json()

	n=data['name']
	loc=data['location']
	rList=data["randomList"]

	return jsonify({'result':'Success', 'name':n, 'location':loc,\
		'ranList':rList[1]})



@app.route('/viewresults')
def viewresults():
	db=get_db()
	cur=db.execute('select id, name,location from users')
	results=cur.fetchall()
	return '<h1>The ID is {}. The name is {}. The location is {}\
	</h1>'.format(results[3]['id'],results[3]['name'],results[3]['location'])

if __name__=='__main__':
	app.run()
