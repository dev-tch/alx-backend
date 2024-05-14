#!/usr/bin/env python3
""" module flask to render message in html """
from flask import Flask, render_template, g
from flask_babel import Babel
from flask import request
from typing import (Union, Dict)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id_user: str) -> Union[Dict[str, str], None]:
    """ return user associated for table users"""
    try:
        if id_user is not None and isinstance((index := int(id_user)), int):
            return users.get(index, None)
    except ValueError:
        return None


class Config:
    """ class to config Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """ decorator excuted before request action to save user data"""
    id_user: str = request.args.get('login_as', None)
    user = get_user(id_user)
    if user is not None and isinstance(user, Dict) and "name" in user:
        setattr(g, 'login_as', user)


@babel.localeselector
def get_locale():
    """get the languague used for translation"""
    locale_param = request.args.get('locale', None)
    if locale_param is not None and locale_param in Config.LANGUAGES:
        return locale_param
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
@app.route('/<locale>', strict_slashes=False)
@app.route('/<login_as>', strict_slashes=False)
def hello_world():
    """render htm page  5-index"""
    user = getattr(g, 'login_as', None)
    username = user["name"] if user is not None else ""
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    """ Main Flask """
    app.run(host='0.0.0.0', port=5000)