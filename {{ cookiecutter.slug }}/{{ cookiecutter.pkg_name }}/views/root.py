from flask import render_template

from . import blueprint as bp


@bp.route("/")
def root():
    return render_template("index.html")
