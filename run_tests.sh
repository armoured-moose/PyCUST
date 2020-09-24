#!/bin/env bash

#install step here or line below
export PYTHONPATH=PyCUST:$PYTHONPATH
pytest -s tests/basic.py