from alembic.migration import MigrationContext
from alembic.script import ScriptDirectory
from flask import current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from {{ cookiecutter.pkg_name }}.utils import import_all


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(db=db)

import_all("{{ cookiecutter.pkg_name }}.models")


def get_current_revision():
    """Get the current database revision."""
    engine = current_app.extensions["migrate"].db.engine
    with engine.connect() as connection:
        alembic_context = MigrationContext.configure(connection)
        return alembic_context.get_current_revision()


def get_latest_revision():
    # Get the most up-to-date database revision
    config = current_app.extensions["migrate"].migrate.get_config()
    script_dir = ScriptDirectory.from_config(config)
    return script_dir.get_current_head()
