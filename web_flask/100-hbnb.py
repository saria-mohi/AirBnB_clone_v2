#!/usr/bin/python3
""" task on flask with model"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Route /hbnb_filters and use the 8-index.html to display data"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities, places = places)


@app.teardown_appcontext
def teardown(exception):
    """
    Tearsdown the db connection
    """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
