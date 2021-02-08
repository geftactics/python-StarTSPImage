#!/bin/bash

# gitpush > git release > this!

rm -rf StarTSPImage.egg-info
rm -rf dist
python3 setup.py sdist
pip3 install twine
twine upload dist/*
