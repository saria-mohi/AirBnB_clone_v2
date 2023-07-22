#!/usr/bin/python3
""" First task on flask"""
from flask import Flask

app = Flask(__name__)

# this rout by default called when run it
@app.route("/")
def display():
    return("Hello HBNB!")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)