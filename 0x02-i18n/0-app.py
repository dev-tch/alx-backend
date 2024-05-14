#!/usr/bin/env python3
""" module flask to render message in html """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """render htm page  index"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Flask """
    app.run(host='0.0.0.0', port=5000)
