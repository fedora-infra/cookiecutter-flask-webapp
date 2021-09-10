import os
from logging.config import dictConfig

from flask import Flask
from flask_healthz import healthz
from flask_wtf.csrf import CSRFProtect
from whitenoise import WhiteNoise

from {{ cookiecutter.pkg_name }}.database import db, migrate
from {{ cookiecutter.pkg_name }}.l10n import babel
from {{ cookiecutter.pkg_name }}.views import blueprint


# Forms
csrf = CSRFProtect()


def create_app(config=None):
    """See https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/"""

    app = Flask(__name__)

    # Load default configuration
    app.config.from_object("{{ cookiecutter.pkg_name }}.defaults")

    # Load the optional configuration file
    if "FLASK_CONFIG" in os.environ:
        app.config.from_envvar("FLASK_CONFIG")

    # Load the config passed as argument
    app.config.update(config or {})

    if app.config.get("TEMPLATES_AUTO_RELOAD"):
        app.jinja_env.auto_reload = True

    # Logging
    if app.config.get("LOGGING"):
        dictConfig(app.config["LOGGING"])

    # Extensions
    babel.init_app(app)
    app.jinja_env.add_extension("jinja2.ext.i18n")
    csrf.init_app(app)

    # Database
    db.init_app(app)
    migrate.init_app(app, directory=os.path.join(app.root_path, "migrations"))

    # Register views
    app.register_blueprint(blueprint)
    app.register_blueprint(healthz, url_prefix="/healthz")

    # Static files
    app.wsgi_app = WhiteNoise(
        app.wsgi_app, root=f"{app.root_path}/static/", prefix="static/"
    )

    return app
