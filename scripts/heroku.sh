#!/bin/bash
python3 manage.py db upgrade
gunicorn app:app -w 1
