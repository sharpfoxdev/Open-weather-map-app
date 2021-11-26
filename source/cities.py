#!/usr/bin/env python3
"""Modult with functions for adding, removing, searching and listing saved cities"""
import os
import sys
import json

def store(full_path, cities_file_json, cities_file_txt, city_id):
    """Parses cities by their id"""
    if not city_id.isdigit():
        print("Not a number", file=sys.stderr)
        sys.exit(2)
        return
    if not os.path.isdir(full_path):
        os.makedirs(full_path)
    file_path = os.path.join(full_path, cities_file_txt)
    json_path = os.path.join(full_path, cities_file_json)
    parsed_data = ""
    if not is_unique_id(full_path, cities_file_txt, city_id): #checking if ID already exists in file
        print("Id was already added.")
        return
    with open(json_path) as json_file:
        preparsed_data = json.load(json_file)
        parsed_data = parse_data(preparsed_data, city_id)
    if parsed_data == "":
        print("City Id was not found", file=sys.stderr)
        sys.exit(2)
        return
    # Open file and append data to the end of file
    with open(file_path, "a+") as cities:
        cities.write(parsed_data + "\n") #writes data in parsed format

def parse_data(json_file, city_id):
    """Prepare data from json file and format them"""
    data = ""
    for i in json_file:
        if i['id'] == int(city_id):
            data = str(city_id) + " " + i['name'] + " " + i['country']
            return data
    return data

def is_unique_id(full_path, cities_file_txt, city_id):
    """Checks if id is already in file"""

    file_path = os.path.join(full_path, cities_file_txt)
    if not os.path.isfile(file_path): #File doesnt exist yet : first write
        return True
    with open(file_path, "r") as cities:
        for line in cities:
            stripped_line = line.strip() #deleting white spaces
            #returns first collumn and checking if its already there
            if stripped_line.split(' ')[0] == city_id:
                return False
    return True

def search(full_path, cities_file_json, search_string):
    """Searches cities by their name"""
    json_path = os.path.join(full_path, cities_file_json)
    found_lines = 0
    with open(json_path) as json_file:
        parsed_json = json.load(json_file)
        for line in parsed_json:
            if search_string in line['name'].lower():
                print("{0} {1} {2}".format(str(line['id']), line['country'], line['name']))
                found_lines += 1
    if found_lines == 0:
        print("No cities found")

def list_cities(full_path, cities_file_txt):
    """Lists saved cities"""
    file_path = os.path.join(full_path, cities_file_txt)
    if not os.path.isfile(file_path):
        print("You have not saved any cities yet. Use option 'add' to add new city in the list")
        sys.exit(1)
        return
    with open(file_path) as cities:
        for line in cities:
            array = line.strip().split()
            print("{0}: {1} ({2})".format(array[0], " ".join(array[1:-1]), array[-1]))

def remove(full_path, cities_file_txt, city_id):
    """Removes city from saved cities"""
    file_path = os.path.join(full_path, cities_file_txt)
    if not os.path.isfile(file_path):
        print("You have not saved any cities yet. Use option 'add' to add new city in the list")
        sys.exit(1)
        return
    with open(file_path, "r+") as cities:
        data = cities.readlines()
        cities.seek(0)
        for line in data:
            if line.split()[0] != city_id:
                cities.write(line)
        cities.truncate()
