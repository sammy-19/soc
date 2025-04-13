#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies
pip install -r requirements.txt

# Run collectstatic (use python3 and add --noinput)
python3 manage.py collectstatic --noinput