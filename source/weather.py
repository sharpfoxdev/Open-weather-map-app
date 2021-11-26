#!/usr/bin/env python3
"""Module with functions for getting and printing current weather and forecast"""
import sys
import os
import datetime
import requests

def get_current_and_forecast(full_path, cities_file_txt, key):
    """goes through saved cities and for each prints current weather and forecast
    for two days"""
    file_path = os.path.join(full_path, cities_file_txt)
    if not os.path.isfile(file_path):
        print("You have not saved any cities yet. Use option 'add' to add new city in the list")
        sys.exit(2)
        return
    with open(file_path) as cities:
        try:
            for city in cities:
                array = city.strip().split()
                city_id = array[0]
                city_name = " ".join(array[1:-1])#cities with more words in their name
                print("{0}: {1}".format(city_name, get_current(city_id, key))) #current weather
                for i in range(2): #next two days
                    #add 1 and then 2 days to today date
                    date = datetime.date.today() + datetime.timedelta(days=(i+1))
                    date_with_time = str(date) + " 12:00:00"
                    print(" {0}: {1}".format(date, get_forecast(city_id, key, date_with_time)))
        except KeyError:
            print("Something went wrong. You possibly registered invalid api key.", file=sys.stderr)
            sys.exit(2)

def get_current(city_id, api_key):
    """returns current weather for given city"""
    result = make_owm_request('weather', id=city_id, appid=api_key) #returns json data
    description = result['weather'][0]['description'] #getting info from json
    temperature = round(result['main']['temp']-273)
    return str(description + ", " + str(temperature) + "°C")


def get_forecast(city_id, api_key, date):
    """returns forecast for given date in given city"""
    full_forecast = make_owm_request('forecast', id=city_id, appid=api_key) #returns json data
    forecast_for_date = 0 #we want to find forecast for given date in the json data
    for i in full_forecast['list']:#iterate list of days
        if i['dt_txt'] == date: #found correct date
            forecast_for_date = i
    if forecast_for_date == 0: #didnt find correct date
        print("Couldnt find forecast for this day correct date")
        sys.exit(2)
    description = forecast_for_date['weather'][0]['description']
    temperature = round(forecast_for_date['main']['temp']-273)
    return str(description + ", " + str(temperature) + "°C")


def  make_owm_request(path, **kwargs):
    """makes API call"""
    params = dict(**kwargs)
    result = requests.get('https://api.openweathermap.org/data/2.5/' + path, params=params)
    return result.json()
