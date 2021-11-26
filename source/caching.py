#!/usr/bin/env python3
"""Module that gets json data about cities from open weather map website"""
import gzip
import os
import requests

def get_city_list(full_path, file_name):
    """enter the full path to the directory with the file, excluding the
    filename in the path, and then the file name itself"""
    if not os.path.isdir(full_path): #path to the directory with file didnt exist
        os.mkdir(full_path)
    file_path_city = os.path.join(full_path, file_name) #path to the file
    if not os.path.isfile(file_path_city): #file does not exist
        #download, decompress and save to the file the list of cities
        result = requests.get('http://bulk.openweathermap.org/sample/city.list.json.gz')
        content = gzip.decompress(result.content).decode('utf-8')
        with open(file_path_city, 'w') as cities:
            cities.write(content)
