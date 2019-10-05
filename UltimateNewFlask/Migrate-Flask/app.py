from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/abdlmalik/Desktop/Flask/UltimateFlask/Migrate-Flask/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEBUG']=True

db=SQLAlchemy(app)
migrate=Migrate(app,db)

manager=Manager(app)
manager.add_command('db',MigrateCommand)


class Member(db.Model):

	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50))
	subscribed=db.Column(db.Boolean)


class Orders(db.Model):

	id=db.Column(db.Integer,primary_key=True)
	total=db.Column(db.Integer)

if __name__=="__main__":
	manager.run()
	