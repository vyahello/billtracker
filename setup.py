"""Entrypoint API for a module."""
import os
from typing import IO, Sequence
from setuptools import setup, find_packages
from billtracker import __author__, __email__, __version__, __name__ as __package_name__


def __file_to_string(name: str) -> str:
    """Converts file content into string format

    Args:
        name: name of a file

    Returns:
        file content as a string
    """
    here: str = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, name)) as file:  # type: IO[str]
        return file.read()


def __iterable_from_file(name: str) -> Sequence[str]:
    """Returns a list of iterable sequence.

    Args:
        name: name of a file
    """
    with open(name) as stream:  # type: IO[str]
        return tuple(map(str.strip, stream.readlines()))


def __readme() -> str:
    """Returns 'README.md' file content."""
    return __file_to_string("README.md")


def __changelog() -> str:
    """Returns 'CHANGELOG.txt' file content."""
    return __file_to_string("CHANGELOG.md")


def __long_description() -> str:
    """Returns project long description."""
    return f"{__readme()}\n\n{__changelog()}"


def __requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    return __iterable_from_file("requirements.txt")


def __requirements_for_development() -> Sequence[str]:
    """Returns development requirements sequence."""
    return __iterable_from_file("requirements-dev.txt")


if __name__ == "__main__":
    setup(
        name=__package_name__,
        version=__version__,
        description="A tool to track users bills",
        long_description=__long_description(),
        classifiers=(
            "Programming Language :: Python",
            "Framework :: Pyramid",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ),
        author=__author__,
        author_email=__email__,
        keywords="web pyramid pylons",
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        extras_require={"testing": __requirements_for_development()},
        install_requires=__requirements(),
        entry_points={"paste.app_factory": ("main = billtracker:main",)},
    )
