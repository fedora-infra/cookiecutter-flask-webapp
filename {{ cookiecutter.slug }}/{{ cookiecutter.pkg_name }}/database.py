"""
Use sqlalchemy-helpers.

Import the functions we will use in views and in migrations.
"""

from sqlalchemy_helpers import Base, exists_in_db, get_or_create, is_sqlite  # noqa
from sqlalchemy_helpers.flask_ext import (  # noqa
    DatabaseExtension,
    first_or_404,
    get_or_404,
    get_url_from_app,
)


db = DatabaseExtension()
