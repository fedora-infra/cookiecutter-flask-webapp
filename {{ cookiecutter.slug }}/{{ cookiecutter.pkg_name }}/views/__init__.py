from flask import Blueprint

from {{ cookiecutter.pkg_name }}.utils import import_all


blueprint = Blueprint("root", __name__)
import_all("{{ cookiecutter.pkg_name }}.views")
