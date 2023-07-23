#!/usr/bin/python3
""" task on flask with model"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    # Inserts all States
    storall_state = storage.all("State").values()
    return (render_template('7-states_list.html', states=storall_state))


@app.teardown_appcontext
def teardown(exception):
    """
    Tearsdown the db connection
    """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
