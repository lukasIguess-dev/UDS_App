import requests
import json


def get_data():
    response = requests.get("https://mensaar.de/api/2/TFtD8CTykAXXwrW4WBU4/1/de/getMenu/sb")
    data = response.json()

    file = open("json_data.json", "w")

    json.dump(data, file, indent=4)

    file.close()
