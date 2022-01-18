#!/bin/bash


main() {
:<<DOC
    Launches 'main' billtracker executor.
DOC
  python setup.py develop
  pserve development.ini
}


main
