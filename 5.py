

car = {"make": "Toyota", "model": "Camry", "year": 2020, "color": "Blue"}
print("Car model:", car["model"])


car["owner"]= "Rahul"
print("Updated car dictionary:", car)

#ჩემი მეორე ვერსია
car = {}
car["make"] = "Toyota"
car["model"] = "Camry"
car["year"] = 2020
car["color"] = "Blue"
print("Car model:", car["model"])
car["owner"] = "Rahul"
print("Updated car dictionary:", car)

print("*******************************************************************")

#CHATGPT VERSION

car = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
}

print(f"Car model: {car['model']}")

car["owner"] = "Rahul"
print(f"Updated car dictionary: {car}")