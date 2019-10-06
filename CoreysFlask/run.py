
from flask import Flask,render_template,url_for,flash,redirect
from secrets import token_hex as tok


from flaskblog import app




if __name__ == '__main__':
    app.run(debug=True)