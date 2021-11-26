#!/usr/bin/env python3
"""module with functions regarding storing and retrieving api key"""
import os
import sys

def store_key(full_path, file_name, key):
    """stores key"""
    if not os.path.isdir(full_path):
        os.makedirs(full_path)
    file_key = os.path.join(full_path, file_name)
    with open(file_key, 'w') as file:
        file.write(key)

def retrieve_key(file_path, file_name):
    """returns key"""
    try:
        with open(file_path + file_name) as key:
            return key.read()
    except FileNotFoundError:
        print('Key was not found, are you sure \
you registered through my_owm register <key>?', file=sys.stderr)
        sys.exit(2)
