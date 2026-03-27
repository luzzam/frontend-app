# utils.py

import os
import json
from datetime import datetime

def load_json_file(file_path):
    """Loads a JSON file from the given path."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(data, file_path):
    """Saves data to a JSON file at the given path."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_current_timestamp():
    """Returns the current timestamp in the format 'YYYY-MM-DD HH:MM:SS'."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def is_valid_email(email):
    """Checks if the given email is valid."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

def get_absolute_path(relative_path):
    """Gets the absolute path of a file or directory given a relative path."""
    return os.path.abspath(relative_path)