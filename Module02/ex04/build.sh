#!/bin/bash

python -m pip install --upgrade pip setuptools wheel build
python -m build
python -m pip install ./dist/my-minipack-1.0.0.tar.gz