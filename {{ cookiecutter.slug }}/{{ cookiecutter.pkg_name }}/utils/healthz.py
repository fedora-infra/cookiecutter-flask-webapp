from flask_healthz import HealthError

from {{ cookiecutter.pkg_name }}.database import get_current_revision, get_latest_revision


def liveness():
    pass


def readiness():
    latest = get_latest_revision()
    try:
        current = get_current_revision()
    except Exception as e:
        raise HealthError(f"Can't get the database revision: {e}")
    if current is None:
        raise HealthError("Can't connect to the database")
    if current != latest:
        raise HealthError("The database schema needs to be updated")
