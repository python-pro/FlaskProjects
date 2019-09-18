from app import app
from flask import render_template




@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/jinja")
def jinja():

	my_name="AbdulMalik"


	# Integers
	my_age = 30

	# Lists
	langs = ["Python", "JavaScript", "Golang", "Java", "C++", "Rust"]

	# Dictionaries
    friends = {"Tony": 43,"Cody": 28,"Amy": 26,"Clarissa": 23,"Wendell": 39}

	
    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty


	return render_template("public/jinja.html",name=my_name,my_age=my_age, langs=langs,
    friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
    my_remote=my_remote, repeat=repeat)

	


	


	
	
    

@app.route("/about")
def about():
    return "<h3 style='color :orange'>In this page you can have a lot of info about my page</h3>"