#!/usr/bin/env bash

PACKAGE="billtracker"


entry-point-box() {
:<<DOC
    Provides pretty-printer check box
DOC
    echo "Start ${1} analysis ..."
}


remove-pycache() {
:<<DOC
    Removes python cache directories
DOC
    ( find . -depth -name __pycache__ | xargs rm -r )
}


check-black() {
:<<DOC
    Runs "black" code analyser
DOC
    entry-point-box "black" && ( black --check ./ )
}


check-flake8() {
:<<DOC
    Runs "flake8" code analysers
DOC
    entry-point-box "flake" && ( flake8 ${PACKAGE} )
}


check-flakehell() {
:<<DOC
    Runs "flakehell" code analysers
DOC
    entry-point-box "flakehell" && ( flakehell lint )
}


check-flake() {
:<<DOC
    Runs "flake8" code analysers
DOC
    check-flake8 && check-flakehell
}


check-pylint() {
:<<DOC
    Runs "pylint" code analyser
DOC
    entry-point-box "pylint" && ( pylint $(find ./ -iname *.py) )
}


check-mypy() {
:<<DOC
    Runs "mypy" code analyser
DOC
    entry-point-box "mypy" && ( mypy --package "${PACKAGE}" )
}


check-docstrings() {
:<<DOC
     Runs "pydocstyle" static documentation code style formatter
DOC
    entry-point-box "pydocstyle" && ( pydocstyle --explain --count ${PACKAGE} )
}


check-unittests() {
:<<DOC
    Runs unittests using "pytest" framework
DOC
    entry-point-box "unitests" && pytest && python -m unittest
}


main() {
:<<DOC
    Runs "main" code analyser
DOC
    (
      remove-pycache
      check-black && \
      check-mypy && \
      check-pylint && \
      check-docstrings && \
      check-unittests
    )
}


main
