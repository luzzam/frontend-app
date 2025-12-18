import logging
import os
from datetime import datetime

def configure_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('frontend-app.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_environment_variable(var_name):
    return os.getenv(var_name)

def is_debug_mode():
    return get_environment_variable('DEBUG_MODE') == 'True'

def validate_input_data(data):
    if not isinstance(data, dict):
        raise ValueError('Input data must be a dictionary')
    required_keys = ['name', 'email']
    for key in required_keys:
        if key not in data:
            raise ValueError(f'Missing required key: {key}')
    return data

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# example usage
if __name__ == '__main__':
    logger = configure_logger('frontend-app')
    logger.info('Logger configured')
    print(get_current_timestamp())
    print(get_environment_variable('PATH'))
    print(is_debug_mode())
    try:
        validate_input_data({'name': 'John Doe', 'email': 'john@example.com'})
    except ValueError as e:
        logger.error(str(e))
    write_to_file('example.txt', 'Hello World!')