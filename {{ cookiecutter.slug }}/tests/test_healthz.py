import flask_migrate
import pytest
from alembic.script import ScriptDirectory
from flask import current_app

from {{ cookiecutter.pkg_name }}.database import db, get_current_revision


def test_healthz_liveness(client):
    """Test the /healthz/live check endpoint"""
    response = client.get("/healthz/live")
    assert response.status_code == 200
    assert response.json == {"status": 200, "title": "OK"}


def test_healthz_readiness_ok(client):
    """Test the /healthz/ready check endpoint"""
    response = client.get("/healthz/ready")
    print(response.data)
    assert response.status_code == 200
    assert response.json == {"status": 200, "title": "OK"}


def test_healthz_readiness_unavailable(client, mocker, tmpdir):
    """Test the /healthz/ready check endpoint when the DB is not ready"""
    db.drop_all()
    mocker.patch.dict(
        current_app.config, {"SQLALCHEMY_DATABASE_URI": f"sqlite:///{tmpdir}/new.db"}
    )
    response = client.get("/healthz/ready")
    assert response.status_code == 503
    assert response.json == {"status": 503, "title": "Can't connect to the database"}


def test_healthz_readiness_needs_upgrade(client):
    """Test the /healthz/ready check endpoint when the DB schema is old"""
    # Find the earliest revision
    config = current_app.extensions["migrate"].migrate.get_config()
    script_dir = ScriptDirectory.from_config(config)
    base_rev = script_dir.get_base()
    current_rev = get_current_revision()
    if current_rev == base_rev:
        pytest.skip("Only one DB revision at the moment.")
    # Stamp it.
    flask_migrate.stamp(revision=base_rev)
    response = client.get("/healthz/ready")
    assert response.status_code == 503
    assert response.json == {
        "status": 503,
        "title": "The database schema needs to be updated",
    }


def test_healthz_readiness_exception(client, mocker):
    """Test the /healthz/ready check endpoint when the DB is wrong"""
    mocker.patch.dict(
        current_app.config, {"SQLALCHEMY_DATABASE_URI": "sqlite:////does/not/exist"}
    )
    response = client.get("/healthz/ready")
    assert response.status_code == 503
    assert response.json["status"] == 503
    assert response.json["title"].startswith(
        "Can't get the database revision: (sqlite3.OperationalError) "
        "unable to open database file"
    )
