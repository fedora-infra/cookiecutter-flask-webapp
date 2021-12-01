from flask import render_template

from {{ cookiecutter.pkg_name }}.models import User

from . import blueprint as bp


@bp.route("/")
def root():
    users = User.query.all()
    return render_template("index.html", users=users)
