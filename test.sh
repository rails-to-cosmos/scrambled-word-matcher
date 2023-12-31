#!/bin/bash

set -e

if [[ "$*" == *"-k"* ]]; then
    echo "Running specific test case (skip other checks)"
else
    pipenv run mypy scrambled_word_matcher
    pipenv run python scrambled_word_matcher/run_doctests.py
fi

pipenv run pytest . --verbose $@
