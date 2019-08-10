# B_R_R
# M_S_A_W

from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return '<h1 style="font-size:60px;">Welcome to my WebPage</h1>'



@app.route('/about')
def about():
    return '<h3 style="color: green;">Information about the page</h3>'





if __name__=='__main__':
    app.run()