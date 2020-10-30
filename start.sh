#!/bin/sh

python tp_iw/manage.py migrate
python tp_iw/manage.py runserver 0.0.0.0:8000