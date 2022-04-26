import json

# open the file in python
with open("D:\\Api data\\EmployeeData.JSON") as x:
    file = json.load(x)

    for i in file:
        if i["id"] == 1005:

         assert i["name"] == "Test 3"
         print(i["coverPicture"])
