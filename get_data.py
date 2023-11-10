import requests
import json


def get_data():
    return MensaarData()


class MensaarData:
    def __init__(self):
        response = requests.get("https://mensaar.de/api/2/TFtD8CTykAXXwrW4WBU4/1/de/getMenu/sb")
        self.__data = response.json()

    def get_today(self):
        for day in self.__data["days"]:
            if not day["isPast"]:
                return day

    def get_meals(self, day):
        date = day["date"]
        __counters = day["counters"]
        menu1 = __counters[0]
        menu2 = __counters[1]
        menu3 = __counters[2]


class Menu:
    def __init__(self, name: str, data: json):
        self.name = name
        self.__data = data

    def display_name(self):
        return self.__data["displayName"]

    def aufgang(self) -> str:
        return self.__data["description"]

    def meal(self):
        meal = self.__data["meals"][0]
        meal_name = meal["name"]
        meal_components = meal["components"]
        return {"name": meal_name,
                "components": meal_components
                }


class Day:
    def __init__(self, date: str, menu1: Menu, menu2: Menu, menu3: Menu):
        self.date = date
        self.m1 = menu1
        self.m2 = menu2
        self.m3 = menu3
