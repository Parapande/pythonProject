import json

data ='''{"id": 12,
    "email": "rachel.howell@reqres.in",
        "first_name": "Rachel",
        "last_name": "Howell",
        "avatar": "https://reqres.in/img/faces/12-image.jpg",
        "languages": ["java", "python"]}'''
print(type(data))
data2=json.loads(data)
print(type(data2))

info=data2["first_name"]
print(info)

print(data2["avatar"])

infos=data2["languages"][1]
print(type(infos))
print(infos)
print(data2["email"])
