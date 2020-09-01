#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask
# create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_flask():
    """displays Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
