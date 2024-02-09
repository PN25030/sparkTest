#!/bin/bash

# Name of the virtual environment
venv_name="myenv"

# Create virtual environment
python3 -m venv "$venv_name"

# Activate virtual environment
source "$venv_name/bin/activate"

# Install requirements from requirements.sh
if [ -f "requirements.sh" ]; then
    bash requirements.sh
else
    echo "Error: requirements.sh not found."
    exit 1
fi

# Deactivate virtual environment
deactivate
