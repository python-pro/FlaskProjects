from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SECRET_KEY']='57ba628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


from flaskblog import routes