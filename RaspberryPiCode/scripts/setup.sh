#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements/requirements.txt
pip install -r requirements/requirements2.txt
pip install wheel
pip install pycocotools@git+https://github.com/gautamchitnis/cocoapi.git@cocodataset-master#subdirectory=PythonAPI
pip install imageai --upgrade