
from flask import Flask,render_template,url_for
from secrets import token_hex as tok
from forms import RegistrationForm, LoginForm




app = Flask(__name__)


app.config['SECRET_KEY']=tok(16)


posts = [
    {
        'author': 'AbdulMalik Sharif',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'AbdALLAH Sharif',
        'title': 'Blog Post New',
        'content': 'First post content',
        'date_posted': 'June 5, 2021'
    },
    {
        'author': 'Sumayya Sharif',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 2, 2020'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register")
def register():
	form=RegistrationForm()
	return render_template('register.html',title='Register',form=form)



@app.route("/login")
def login():
	form=LoginForm()
	return render_template('login.html',title='Login',form=form)




if __name__ == '__main__':
    app.run