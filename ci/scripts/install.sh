#!/bin/sh
set -e

# build to create the dist
poetry build

# install the built package via pipx
pipx install -f dist/*.tar.gz
