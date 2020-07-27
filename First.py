from flask import Flask, redirect, url_for, render_template, request

# Instance of flask web application
app = Flask(__name__)

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
		user = request.form["name"]
		return redirect(url_for("user", usr=user))
	else:
		return render_template("login.html")

@app.route("/<usr>")
def user(usr):
	return "<h1>{usr}</h1>"

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