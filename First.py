from flask import Flask, redirect, url_for

# Instance of flask web application
app = Flask(__name__)

@app.route("/")
# Defining the pages on the website
def home():
	return "Hello World!"

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.route("/admin")
def admin():
	# Redirect to another page
	return redirect(url_for("home"))

# Run the app
if __name__== "__main__":
	app.run()