from flask import render_template

from {{ cookiecutter.pkg_name }}.models import User

from . import blueprint as bp


@bp.route("/")
def root():
    users = User.query.all()
    return render_template("index.html", users=users)


@bp.route("/user/<int:user_id>")
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("profile.html", user=user)
