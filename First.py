from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedata

# Instance of flask web application
app = Flask(__name__)

# Secret Key
app.secret_key = "hello"

app.permanent_session_lifetime = timedata(days=5)

# Dynamic
# @app.route("/<name>")
@app.route("/")
# Defining the pages on the website
# def home(name):
def home():
	# return "Hello World!"
	# return render_template("index.html", content=name)
	# return render_template("index.html", content=["tim", "joe", "gorge"])
	return render_template("index.html")

@app.route("/test")
def test():
	return render_template("new.html", content="Testing")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["name"]
		session["user"] = user
		flash("Login Successful!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already LoggedIn")
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		# return f"<h1>{user}</h1>"
		return render_template("user.html", user=user)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	# if "user" in session:
	# 	user = session["user"]
	# 	flash("You have been logged out, {user}", "info")
	flash("You have been logged out", "info")
	session.pop("user", None)
	return redirect(url_for("login"))

# @app.route("/<name>")
# def user(name):
# 	return f"Hello {name}!"

# @app.route("/admin")
# def admin():
# 	# Redirect to another page
# 	# return redirect(url_for("home"))
# 	return redirect(url_for("user", name="Admin!"))

# Run the app
if __name__== "__main__":
	# Automatically detecting changes and updating the website
	app.run(debug=True)