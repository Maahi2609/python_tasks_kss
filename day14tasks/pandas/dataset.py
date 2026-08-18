'''A dataset contains city populations:
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
Scenario:
You want data for:
["Delhi", "Chennai", "Bangalore"]
Task:
● Create a Series with the above index
● Identify which cities have missing values (NaN)'''

import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
cities_series = pd.Series(cities)
my_cities = ["Delhi", "Chennai", "Bangalore"]
my_city_series = pd.Series(cities, index = my_cities)
print(my_city_series)
