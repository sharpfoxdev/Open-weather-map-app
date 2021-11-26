#!/usr/bin/env python3
"""Main module of the app, calls other modules when needed"""

import sys
import os
import source.caching as caching
import source.key as key
import source.cities as cities
import source.weather as weather

#caching list of cities
CACHE_BASE = os.path.expanduser("~/.cache/open_weather_map_drivers/")
FILE_CITIES_JSON = "cities.json"
FILE_CITIES_TXT = "cities.txt"

#path for storting API KEY
API_BASE = os.path.expanduser("~/.config/owm-Drivers/key/")
FILE_API = "owm.key"

def list_cities():
    """lists cities saved in FILE_CITIES_TXT in folder CACHE_BASE"""
    cities.list_cities(CACHE_BASE, FILE_CITIES_TXT)

def add_city(city_id):
    """adds city to FILE_CITIES_TXT in folder CACHE_BASE"""
    caching.get_city_list(CACHE_BASE, FILE_CITIES_JSON) #to make sure the json file exists
    cities.store(CACHE_BASE, FILE_CITIES_JSON, FILE_CITIES_TXT, city_id)

def register_api_key(api_key):
    """registers api key into FILE_API in folder API_BASE"""
    key.store_key(API_BASE, FILE_API, api_key)

def search_city(city):
    """searches city in FILE_CITIES (json file) and prints matches"""
    caching.get_city_list(CACHE_BASE, FILE_CITIES_JSON)
    cities.search(CACHE_BASE, FILE_CITIES_JSON, city.lower())

def remove_city(city_id):
    """removes city from FILE_CITIES_TXT"""
    cities.remove(CACHE_BASE, FILE_CITIES_TXT, city_id)

def get_weather():
    """prints current weather and forecast for two days for all cities in FILE_CITIES_TXT"""
    api_key = key.retrieve_key(API_BASE, FILE_API)
    weather.get_current_and_forecast(CACHE_BASE, FILE_CITIES_TXT, api_key)

def parse_arguments():
    """parses arguments and decides, which subcommand was used"""
    if len(sys.argv) == 3: #possibilities are rm, add, search, register
        two_arguments()
    elif len(sys.argv) == 2: #only possibility is list
        one_argument()
    elif len(sys.argv) == 1: #called without arguments
        get_weather()
    else:
        print("Invalid input.", file=sys.stderr)
        sys.exit(2)
        return

def one_argument():
    """there was given one argument when the code was executed"""
    if sys.argv[1] == "list":
        list_cities()
    else:
        print("Invalid input.", file=sys.stderr)
        sys.exit(2)
        return

def two_arguments():
    """there were given two arguments, when the code was executed"""
    if sys.argv[1] == "rm":
        remove_city(sys.argv[2])
    elif sys.argv[1] == "search":
        search_city(sys.argv[2])
    elif sys.argv[1] == "add":
        add_city(sys.argv[2])
    elif sys.argv[1] == "register":
        register_api_key(sys.argv[2])
    else:
        print("Invalid input.", file=sys.stderr)
        sys.exit(2)
        return

def main():
    """entry point of the code"""
    parse_arguments()

if __name__ == '__main__':
    main()
