# CookieCutter for Fedora Infrastructure webapps

This is a [CookieCutter](https://cookiecutter.readthedocs.io) template directory for
Fedora Infrastructure webapps that are based on Flask.

Use it with:
```
cookiecutter gh:fedora-infra/cookiecutter-flask-webapp
```

It will ask you for the application name and some other variables, and will create the package
structure for you.


## Features

Here are the libraries and services that are integrated:

- Database support with [SQLAlchemy](https://www.sqlalchemy.org/)
  & [Alembic](https://alembic.sqlalchemy.org)
- OpenShift support with [S2I](https://github.com/sclorg/s2i-python-container)
- Formatting with [Black](https://github.com/psf/black),
  [isort](https://github.com/pycqa/isort)
  and [pyupgrade](https://github.com/asottile/pyupgrade)
- Unit tests with [Pytest](https://pytest.org/), [Coverage](https://coverage.readthedocs.io)
  & [Tox](tox.readthedocs.io/)
- Security with [Flask-Talisman](https://pypi.org/project/flask-talisman/)
  & [Bandit](https://github.com/PyCQA/bandit)
- Documentation with [Sphinx](https://www.sphinx-doc.org/)
- Various checks like [flake8](https://github.com/PyCQA/flake8),
  [liccheck](https://github.com/dhatim/python-license-check),
  and [rstcheck](https://github.com/myint/rstcheck)
- [Mergify](https://mergify.io/)
- Github CI and [CentOS CI](https://ci.centos.org/)
- [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
- [Pre-Commit](https://pre-commit.com/)


## Testing

There are some checks to make sure the templated app pass its own unit tests.
You can run those checks with:

```
pytest -s tests
```

