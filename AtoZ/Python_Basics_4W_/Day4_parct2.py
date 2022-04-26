"""# adding data in dishonary

car = {
    "brand": ["bmw","audi"],
    "location": "pune",
    "year": "1996",
    "name": "parag",
    "size of car": "4meter"

}
mycar =car["brand"][0]
print(mycar)
car["light"] = "white"
car["bullet"]="350"
car["bullet"]="550"
car["year"]="2000"
car.pop("locatio","items is not present")
del car["name"]
for key, values in car.items():
    print(key, values, sep=", ")"""

capitals = {"Maharashtra": "Mumbai",
            "Telangana": "Hyderabad",
            "Tamilnadu": "Chennai",
            "Karnataka": "Bengaluru",
            "Bihar": ["Patna", "rameshwar", "lahor"]
            }
# dishnoary contains list
cpa = capitals["Bihar"][-1]
print(cpa)
print(len(capitals))

# add item in dish
cpa = capitals["Up"] = "prayagraj"
print(cpa)
# using loops and items
for key, values in capitals.items():
    print(key, values, sep="-")

# prnt only keys
cp = capitals.keys()
print(cp)

# print valuses
co = capitals.values()
print(co)
