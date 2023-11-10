from get_data import MensaarData


Mensaar = MensaarData()
data = Mensaar.get_today()

meal_date = data["date"]
print(meal_date)