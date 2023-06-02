from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mobile-prototype")
def mobile():
    return render_templates("mobile-prototype.html")

@app.route("/ipad-prototype")
def ipad():
    return render_templates("ipad-prototype.html")

@app.route("/desktop-prototype")
def desktop():
    return render_templates("desktop-prototype.html")