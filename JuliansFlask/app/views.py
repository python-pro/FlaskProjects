from app import app
from flask import render_template




@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/about")
def about():
    return "<h3 style='color :orange'>In this page you can have a lot of info about my page</h3>"