#!/usr/bin/python3
""" task on flask with model"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page from static folder in previous steps"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """
    Tearsdown the db connection
    """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
