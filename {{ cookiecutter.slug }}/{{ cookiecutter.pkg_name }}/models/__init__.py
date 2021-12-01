from {{ cookiecutter.pkg_name }}.database import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.Unicode(254), index=True, unique=True, nullable=False)
    full_name = db.Column(db.Unicode(254), nullable=False)
    timezone = db.Column(db.Unicode(127), nullable=True)
