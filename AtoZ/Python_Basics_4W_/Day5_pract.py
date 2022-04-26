"""# tupple in python

thistuple = ("apple", "banana", "cherry")
# convert tupple in list

c= list(thistuple)
print(type(c))
c.append("mango")
print(thistuple[0:2],c)


for i in thistuple:
    print("apple","this in tupple")

# reverse a tupple
names = ("rajat", "ashish", "ram", "parag")
print(names)

# count method in tupple
p = (names.count("ram"))
print(p)

# by index we will khon the postion of ram
l = names.index("ram")
print(l)

#Exercise 1: Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)
m=list(tuple1)
m.reverse()
print(m)

tuple1=tuple1[::-1]
print(tuple1)

tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple2[1][1])


#two list into dict
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

ps=dict(zip(keys,values))
print(ps)

#copy and update two dict or merge
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
pd = dict1.copy()
dict1.update(dict2)
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": [80,90,0]
            }
        }
    }
}

print(dict1)
"""


car=(sampleDict["class"]["student"]["marks"]["history"][1])
print(car)