"""import json

body = '''{"id": 12,
    "email": "rachel.howell@reqres.in",
        "first_name": "Rachel",
        "last_name": "Howell",
        "avatar": "https://reqres.in/img/faces/12-image.jpg",
        "languages": ["java", "python"]}'''
# Parse data json into dict or list
body1 = json.loads(body)

info = body1["id"]
print(info)

infos = body1["languages"][1]
print(infos)
print(body1["avatar"], ["last_name"])

"""

import json

with open("D:\\Api data\\EmployeeData.JSON") as file:
    # parase the file in python format
    files = json.load(file)

    for i in files:
        if i["id"] == 3039:
         print(i)
         assert i["password"] == "Test@1234"
         print(i["password"])
