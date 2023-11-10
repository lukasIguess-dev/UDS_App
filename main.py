from datetime import date
import time
import json

today = date.fromtimestamp(time.time())

with open("json_data.json", "r") as read_file:
    data = json.load(read_file)

meal_date = data["days"][0]["date"]
meal_2 = data["days"][0]["counters"][3]

print(meal_2)