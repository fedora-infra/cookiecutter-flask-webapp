from flask import g, request
from flask_babel import Babel


LANGUAGES = ["en_US", "fr_FR"]

babel = Babel()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES)


@babel.timezoneselector
def get_timezone():
    user = getattr(g, "user", None)
    if user is not None:
        return user.timezone
