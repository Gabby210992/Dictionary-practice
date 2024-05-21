def new_country(country, visits, cities):
   new_country = {}
   new_country["country"] = countries
   new_country["visits"] = no_of_visits
   new_country["cities"] = list_of_cities
   travel_log.append(new_country)
   print(travel_log)
   
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities":["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

countries = input("Enter the countries you visited: \n")
no_of_visits = int(input("Enter the number of visits: \n"))
list_of_cities = input("Enter the city you visited \n")
new_country(countries, visits = no_of_visits, cities = list_of_cities)