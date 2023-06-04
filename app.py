from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mobile-prototype")
def mobile():
    return render_template("mobile-prototype.html")

@app.route("/ipad-prototype")
def ipad():
    return render_template("ipad-prototype.html")

@app.route("/desktop-prototype")
def desktop():
    return render_template("desktop-prototype.html")