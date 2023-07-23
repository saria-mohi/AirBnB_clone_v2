#!/usr/bin/python3
""" task on flask with model"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states_template_id(id):
    """function that route /states/<id>"""
    state = states = None
    if not id:
        states = list(storage.all(State).values())
    else:
        states = storage.all(State)
        key = "State." + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    return render_template('9-states.html', **locals())


@app.teardown_appcontext
def teardown(exception):
    """
    Tearsdown the db connection
    """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
