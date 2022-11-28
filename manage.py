from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", title="Home")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")

@app.route("/generic", methods=["GET"])
def generic():
    return render_template("generic.html", title="Generic")

@app.route("/elements", methods=["GET"])
def elements():
    return render_template("elements.html", title="Elements")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)