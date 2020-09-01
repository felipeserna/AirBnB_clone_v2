#!/usr/bin/python3
"""
starts a Flask web application
Two routes
C route
Python route
"""


from flask import Flask
# create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_flask():
    """displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """displays C followed by text"""
    x = text.replace("_", " ")
    return ("C {}".format(x))


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """displays Python followed by text"""
    y = text.replace("_", " ")
    return ("Python {}".format(y))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
