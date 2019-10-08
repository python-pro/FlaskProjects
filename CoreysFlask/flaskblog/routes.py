from flask import render_template, url_for, flash, redirect,request
from flaskblog import app,bcrypt,db
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user,current_user,logout_user,login_required



posts = [
    {
        'author': 'AbdulMalik Sharif',
        'title': 'Technical Features of Virtualization',
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashP=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashP)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data}, your account has been created ',"success")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()            
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')

            return redirect(url_for(next_page)) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your email and passwor','danger')
    return render_template('login.html',title='Login',form=form)



@app.route("/logout",methods=["GET","POST"])
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/account", methods=['GET', 'POST'])

def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash("Your account has been successfully updated",'success')
        return redirect(url_for('account'))
    elif request.method=="GET":        
        form.username.data=current_user.username
        form.email.data= current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file,form=form)