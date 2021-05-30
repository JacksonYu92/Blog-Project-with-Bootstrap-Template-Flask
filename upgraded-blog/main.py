from flask import Flask, render_template, request
import requests
import smtplib
import os

My_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

posts=requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()

app =Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone number"]
        message = request.form["message"]
        email_msg = f"name: {name}\nemail: {email}\nphone number: {phone_number}\nmessage: {message}"
        title = "Successfully sent you message"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=My_email, password=password)
            connection.sendmail(
                from_addr=My_email,
                to_addrs=My_email,
                msg=f"Subject:New Message\n\n{email_msg}"
            )
    else:
        title = "Contact Me"
    return render_template("contact.html",title=title)

# @app.route('/form-entry', methods=["POST"])
# def receive_data():
#     name = request.form["name"]
#     email = request.form["email"]
#     phone_number = request.form["phone number"]
#     message = request.form["message"]
#     print(f"name: {name}\nemail: {email}\nphone number: {phone_number}\nmessage: {message}")
#     return "<h1>Successfully sent you message</h1>"


@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    for post in posts:
        if post['id'] == id:
            requested_post = post
    return render_template("post.html", blog_post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

