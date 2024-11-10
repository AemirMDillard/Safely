from flask import Flask, Blueprint, redirect, request, send_file, make_response, render_template, jsonify # type: ignore
import redis # type: ignore
import os

app = Flask(__name__)
r = redis.Redis(host='localhost', decode_responses=True)
messages = []

@app.route("/")
def index():
    '''
        Handles the default route
    '''
    return redirect("/homepage")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/contraceptives")
def contraceptives():
    return render_template("contraceptives.html")

@app.route("/birthcontrol")
def birthcontrol():
    return render_template("birthcontrol.html")

@app.route("/map")
def map():
    return render_template("map.html")

app.run(host="0.0.0.0", port=8022, debug=True)