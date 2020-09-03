#!/usr/bin/python3
"""
starts a Flask web application
HBNB filters
"""


from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
# create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_session(self):
    """after each request removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters(id=None):
    """displays html page"""
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
