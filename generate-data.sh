#!/bin/bash

pushd "$(dirname "$0")"

python3 -m venv dbldatagen_env

source dbldatagen_env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

data-generate

deactivate

popd