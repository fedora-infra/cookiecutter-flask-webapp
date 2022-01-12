import os
from subprocess import run, PIPE

import pytest
from cookiecutter.main import cookiecutter


class Templated:
    def __init__(self, dest_dir):
        assert os.path.exists(dest_dir)
        self.dest_dir = dest_dir
        self.name = os.path.basename(self.dest_dir)
        self.pkgname = self.name.replace("-", "_")

    def run(self, *args, **kwargs):
        env = os.environ.copy()
        env.update({
            "PRE_COMMIT_HOME": os.path.normpath(os.path.join(self.dest_dir, "..", "pre-commit")),
            "POETRY_CACHE_DIR": os.path.normpath(os.path.join(self.dest_dir, "..", "poetry")),
        })
        return run(*args, **kwargs, cwd=self.dest_dir, check=True, env=env, universal_newlines=True)

    def make_git_repo(self):
        self.run(["git", "init", "."])
        self.run(["git", "config", "user.name", "Tests"])
        self.run(["git", "config", "user.email", "tests@example.com"])
        self.run(["git", "add", "."])
        self.run(["git", "commit", "-m", "initial commit"])


@pytest.fixture
def templated(tmpdir):
    dest_dir = cookiecutter(
        ".",
        no_input=True,
        output_dir=tmpdir,
        default_config=True,
        extra_context={
            "name": "Unit Testing Project",
        },
    )
    templated = Templated(dest_dir=dest_dir)
    return templated


def test_basic_creation(templated):
    # We can't have 100% coverage with a templated project
    templated.run(["sed", "-i", "-e", "/^fail_under = 100/d", "pyproject.toml"])
    # Pre-commit wants a Git repo
    templated.make_git_repo()
    # Make sure the unit tests work
    templated.run(["tox"])


def test_alembic_command(templated):
    templated.run(["poetry", "install"])
    # Latest available revision
    result = templated.run(["poetry", "run", "flask", "db", "heads"], stdout=PIPE)
    assert result.stdout.strip() == "initial (head)"
    # Current DB revision when the DB has not been created yet
    result = templated.run(["poetry", "run", "flask", "db", "current"], stdout=PIPE)
    assert result.stdout == ""
    # Create the DB
    templated.run(["poetry", "run", "flask", "db", "upgrade"], stdout=PIPE)
    # Current DB revision when the DB has been created
    result = templated.run(["poetry", "run", "flask", "db", "current"], stdout=PIPE)
    assert result.stdout.strip() == "initial (head)"
