#!/usr/bin/python3
"""
starts a Flask web application
List of states
"""


from models import storage
from models.state import State
from flask import Flask, render_template
# create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_session(self):
    """after each request removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list')
def html_page():
    """displays html page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def html_cities():
    """displays html page"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
