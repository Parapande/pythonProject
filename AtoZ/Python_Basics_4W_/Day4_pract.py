#dishnoary in python print
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mycar=car["brand"]
print(mycar)


mycar=car["model"]
print(mycar)

mycar=car.get("year")
print(mycar)
# using get method to call a key
mycar=car.get("model")
print(mycar)
#using loops

for key,value in car.items():
    print(key,value,sep=", ")

 #using items method
my=car.items()
print(my,sep=", ")

#adding item in dishonary

