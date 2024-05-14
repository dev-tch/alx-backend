#!/usr/bin/env python3
""" module flask to render message in html """
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config:
    """ class to config Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get the languague used for translation"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def hello_world():
    """render htm page  2-index"""
    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Flask """
    app.run(host='0.0.0.0', port=5000)
