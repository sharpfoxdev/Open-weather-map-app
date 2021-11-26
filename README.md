# OPEN WEATHER MAP APPLICATION

- To use this application, you firstly need to install it by running ./install_my_owm.sh in this folder. 

- Then go to https://home.openweathermap.org/users/sign_in, make an account there, get the API key there and copy it to this application by using "my_ssg register <instert_api_key_here>". 

## Possible subcommands

- register <api_key> 		registers API key within application
- search <name_of_city> 	searches for the city to get it's ID
- add <city_ID>		adds chosen city to the list of your bookmarked cities
- list				prints out all of your bookmarked cities
- rm <city_ID>			removes chosen city from the list of bookmarked cities
- when run without any subcommand, the app will print out the current weather and two day forecast for all of your bookmarked cities


## AUTHORS
Made by Michaela Markova, David Truhlar and Michal Trejdl as a task for course Introduction to Linux, NSWI177 at Charles University, 2020. 
