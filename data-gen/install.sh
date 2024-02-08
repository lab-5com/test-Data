#!/bin/bash

python3 -m venv dbldatagen_env

source dbldatagen_env/bin/activate

pip install pyspark
pip install jmespath
pip install numpy
pip install pandas
pip install pyparsing
pip install pyarrow
pip install dbldatagen
pip install --upgrade pip
