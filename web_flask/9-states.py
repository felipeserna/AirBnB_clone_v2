#!/usr/bin/python3
"""
starts a Flask web application
States and State
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


@app.route('/states')
@app.route('/states/<id>')
def states_and_state(id=None):
    """displays html page"""
    states = storage.all(State)
    id_state = None
    state = None
    if id:
        id_state = 'State.' + id
        if id_state in states.keys():
            state = states[id_state]
    return render_template('9-states.html',
                           id=id_state,
                           state=state,
                           states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
