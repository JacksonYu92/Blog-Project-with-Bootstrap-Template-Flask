from flask import Flask, render_template
import requests


posts=requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()

app =Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    for post in posts:
        if post['id'] == id:
            requested_post = post
    return render_template("post.html", blog_post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)