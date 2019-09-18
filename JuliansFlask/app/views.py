from app import app
from flask import render_template




@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/jinja")
def jinja():

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
    repeat=repeat, friends=friends, colors=colors, cool=cool)

	


	


	
	
    

@app.route("/about")
def about():
    return "<h3 style='color :orange'>In this page you can have a lot of info about my page</h3>"