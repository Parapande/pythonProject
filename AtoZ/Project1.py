"""import json

with open("D:\\Api data\\EmployeeData.JSON") as uday:
    file = json.load(uday)

    for i in file:
        if i["id"] == 2011:
            print(i)
            print(i["email"])
            assert i["email"]=="alokpatel@gmail.com"
            print(i["name"])

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": [80, 90, 0,100]
            }
        }
    }
}
uday=sampleDict["class"]["student"]["marks"]["history"][3]
print(uday)
"""