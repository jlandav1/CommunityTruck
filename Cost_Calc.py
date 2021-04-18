import requests
import json
import smtplib
import math
import string
from secret import client_secret

# User inputs the ORIGIN of items that need transport
pick_up_location = input("Please type the item's pick up location?\n").lower()
# User inputs the DESTINATION where items will be transported
drop_off_location = input("Please type the item's drop off location?\n").lower()

# Creates a url to communicate with the Google distance matrix API 
api_key = client_secret

base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
r = requests.get(base_url + 'origins=' + pick_up_location + '&destinations=' + drop_off_location + '&key=' + api_key)

minutes = round((r.json()["rows"][0]["elements"][0]["duration"]["value"]) / 60)
distance = r.json()["rows"][0]["elements"][0]["distance"]["value"]
miles = round(distance * float(0.000621371))


# Sets the TIME rate (dollars/minute) to transport
time_rate = float(0.23)
# Sets the DISTANCE rate (dollars/mile) to transport in truck
distance_rate = float(0.60)
# Sets the LOAD rate (dollars/load) to transport in truck
rate_per_load = 50

# User inputs the number of loads to be taken
loads = input("How many loads will you be taking?\n")

# User inputs whether they will be help with transferring items to truck and from truck to destination. If they will be helping 'yes', they will recieve a $15 discount per load to be transported
help_with_trans = input("Will you be helping with transport? (y/n)\n").lower()
if help_with_trans == 'y' or help_with_trans == 'yes':
    total_cost = round(((time_rate * int(float(minutes))) + (distance_rate * int(miles)) + (rate_per_load * int(loads)) - (15 * int(loads))))
else:
    total_cost = round(((time_rate * int(float(minutes))) + (distance_rate * int(miles)) + (rate_per_load * int(loads))))

# Displays total cost, distance (rounded to the nearest whole #), and time.
print("\nYour total cost = $", total_cost)
print("The total travel time = ", minutes, "mins", "\nThe total travel distance = ", miles, "mil\n")
