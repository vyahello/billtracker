![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Build Status](https://travis-ci.org/vyahello/billtracker.svg?branch=master)](https://travis-ci.org/vyahello/billtracker)
[![Stars](https://img.shields.io/github/stars/vyahello/billtracker)](https://github.com/vyahello/billtracker/stargazers)
[![Forks](https://img.shields.io/github/forks/vyahello/billtracker)](https://github.com/vyahello/billtracker/network/members)
[![Issues](https://img.shields.io/github/issues/vyahello/billtracker)](https://github.com/vyahello/billtracker/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/vyahello/billtracker.svg)](https://GitHub.com/vyahello/billtracker/graphs/watchers/)
[![GitHub contributors](https://img.shields.io/github/contributors/vyahello/billtracker.svg)](https://GitHub.com/vyahello/billtracker/graphs/contributors/)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/billtracker/badge)](https://www.codefactor.io/repository/github/vyahello/billtracker)

# Bills tracker

> A web tool to track your bills built with **pyramid** web framework.

## Tools
- front-end
  - html5
  - css3
- back-end
  - python 3.6 | 3.7 | 3.8
  - [pyramid](https://trypyramid.com/) web framework
  - [sqlalchemy](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) database
  - [alembic](https://alembic.sqlalchemy.org/en/latest/) database migration
  - [nginx](https://www.nginx.com/) web server
  - [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) web interface
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)
  - [travis](https://travis-ci.org) CI

## Usage

Please use [138.68.249.217](http://138.68.249.217/) deployed endpoint.

### Source code

To be able to use and launch app from the source code please execute commands below:

```bash
git clone git@github.com:vyahello/billtracker.git
python setup.py develop
pserve development.ini
```

After please open [0.0.0.0:6543](http://localhost:6543) endpoint to open web app.

![Demo](demo.gif)

## Development notes

Data from [storage](billtracker/storage) folder was generated using https://www.mockaroo.com 

### Database migration

For database migrations [alembic](https://alembic.sqlalchemy.org/en/latest/) package is used. Please follow [alembic.ini](alembic.ini) file for instructions.

Once new changes were made to the database, please follow instructions below:
```bash
alembic revision --autogenerate -m "commit message"
alembic upgrade head
alembic current
```

### Testing

Please follow next command to execute **unit** tests:
```bash
pytest -m unit
```

Or **functional** tests, correspondingly:
```bash
python -m unittests
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_. Please check [AUTHORS](AUTHORS.md) file to see all contributors.

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all development project dependencies