from app import app
from flask import render_template,request,redirect,jsonify,make_response
from datetime import datetime



@app.template_filter("clean_date")
def clean_date(dt):
	return dt.strftime("%d %b %Y")


@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/jinja")
def jinja():
	date = datetime.utcnow()

	def repeat(x, qty=1):
		return x * qty

	my_name="AbdulMalik"

	# Integers
	my_age = 30

	# Lists
	langs = ["Python", "JavaScript", "Golang", "Java", "C++", "Rust"]

	cool = True
	colors = ("Red", "Blue")
	friends = {"Tony": 43,"Cody": 28,"Amy": 26,"Clarissa": 23,"Wendell": 39}
	my_html="<h3>Some random sentence is being generated for testing purpose</h3>"
	
    
        


	

	


	# class GitRemote:
	# 	def __init__(self, name, description, domain):
	# 		self.domain = domain
	# 		self.description = description
	# 		self.name = name

	# 	def clone(self, repo):
 #            return f"Cloning into {repo}"
		
	# 	def pull(self):
	# 		return f"Pulling repo '{self.name}'"     	      
         
                   

 #    my_remote = GitRemote(
 #        name="Learning Flask",
 #        description="Learn the Flask web framework for Python",
 #        domain="https://github.com/Julian-Nash/learning-flask.git"
 #    )



	return render_template("public/jinja.html",name=my_name,my_age=my_age, langs=langs,
    repeat=repeat, friends=friends, colors=colors, cool=cool,date=date,html=my_html)

	


	


	
	
    

@app.route("/about")
def about():
    return "<h3 style='color :orange'>In this page you can have a lot of info about my page</h3>"



@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
	if request.method == "POST":
		username = request.form.get("username")
		email = request.form.get("email")
		password = request.form.get("password")
		print(username,email,password)
		return redirect(request.url)
	return render_template("public/sign_up.html") 
	

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },

	"abdulmalik": {
        "name": "AbdulMalik Sharif",
        "bio": "Creator of the NEW python framework",
        "twitter_handle": "@abdulboss"
    },
	
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):
	user=None
	if username in users:
		user=users[username]
	return render_template("public/profile.html",username=username,user=user)

	

@app.route("/json", methods=["POST"])
def json():
	if request.is_json:
		request.get_json()
		resp = {
            "message": "JSON received from Python Langueage!",
            "sender": request.get_json()["name"]       }
		return make_response(jsonify(resp),200)

	else:
		return make_response(jsonify({"message":"Was not be able to get proper response from python"}),400)


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")



@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    request.get_json()

    print(request.get_json())

    res = make_response(jsonify(request.get_json()), 200)

    return res