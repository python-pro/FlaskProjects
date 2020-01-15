from flask import Flask, render_template,url_for

app=Flask(__name__)


posts=[
    {
      "author": "AbdulMalik Sharif",
      "title": "Blog Post 1",
      "content": "First Post Content",
      "posted_date": "April 8, 2018"
    },
    {
      "author": "Corey Schafer",
      "title": "Blog Post 2",
      "content": "Second Post Content",
      "posted_date": "April 20, 2018"
    },
    {
      "author": "Sumayya Sharif",
      "title": "Blog Post 3",
      "content": "Third Post Content",
      "posted_date": "May 8, 2018"
    },
    {
      "author": "Muhammad Sharif",
      "title": "Blog Post 4",
      "content": "Fourth Post Content",
      "posted_date": "July 13, 2018"
    },
    {
      "author": "Sandtex Python Developer",
      "title": "Blog Post 5",
      "content": "Fifth Post Content",
      "posted_date": "July 22, 2019"
    },
    {
      "author": "Engineer Man Developer",
      "title": "Blog Post 6",
      "content": "Sixth Post Content",
      "posted_date": "July 30, 2019"
    }
  
]


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", posts=posts)



@app.route("/about")
def about():
    return render_template("about.html",title="About")


if __name__=="__main__":
    app.run(debug=True)