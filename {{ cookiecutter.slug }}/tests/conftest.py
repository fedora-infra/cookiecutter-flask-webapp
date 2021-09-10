import os

import flask_migrate
import pytest

from {{ cookiecutter.pkg_name }}.app import create_app
from {{ cookiecutter.pkg_name }}.database import db


@pytest.fixture
def app(tmpdir):
    app = create_app()
    app.config.from_object("tests.app_config")
    # Setup the DB
    db_path = os.path.join(tmpdir, "database.sqlite")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    with app.app_context():
        db.create_all()
        flask_migrate.stamp()
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
