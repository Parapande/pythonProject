# # import json
# # body = '''{"id": 12,
# #     "email": "rachel.howell@reqres.in",
# #         "first_name": "Rachel",
# #         "last_name": "Howell",
# #         "avatar": "https://reqres.in/img/faces/12-image.jpg",
# #         "languages": ["java", "python"]}'''
# # car=json.loads(body)
# # pl=car["id"]
# # print(pl)
# # sd=car["languages"][1]
# # print(sd)
#
# import json
#
# with open("D:\\Api data\\EmployeeData.JSON") as cars:
#     magic = json.load(cars)
#
#     for i in magic:
#         if i["id"] =="3034":
#             print(i)

user=input("enter strinj")

abt=reversed(user)
if list(abt)==list(user):
    print("its an pelenderom")
else:
    print("nit opd")