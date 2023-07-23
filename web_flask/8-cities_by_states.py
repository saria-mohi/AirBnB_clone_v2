#!/usr/bin/python3
""" task on flask with model"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list')
def state_list():
    # Inserts all States
    storall_state = storage.all(State).values()
    return (render_template('7-states_list.html', states=storall_state))


@app.route('/cities_by_states')
def state_list():
    # Inserts all States
    storall_state = storage.all(State).values()
    return (render_template('8-cities_by_states.html', states=storall_state))


@app.teardown_appcontext
def teardown(exception):
    """
    Tearsdown the db connection
    """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
