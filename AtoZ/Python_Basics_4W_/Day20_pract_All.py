# a=[12,23,44,66,78.12,12]
# a.pop(1)
# a.insert(1,"66")
# print(a)
# a.pop(3)
# a.insert(3,"23")
# print(a)


# a.count(23)
# print(a)
# a.append(1233)
# print(a)
# a.extend("12")
# print(a)

# a=0
# b=1
# print(a)
# print(b)
# count=10
# for i in range(0,count):
#     sum=a+b
#     a=b
#     b=sum
#     print(a)


# user=input("enter any \n")
# rev=reversed(user)
#
# if list(user)==list(rev):
#     print("its an palendrom")
# else:
#     print("its not an palendsreom,")

# prime no 3=1,3

# a=int(input("enter no \n"))
# b=[]
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)
#         b.append(i)
# if len(b)==2 or len(b)==1:
#     print("its an prime no")
# else:
#     print("its not prime no")

# s1=int(input("Enter no \n"))
# s2=int(input("Enter no \n"))
# calci=input("ANY oprations on number! \n")
#
# if calci=="+":
#     print(s1+s2)
#
# elif calci=="-":
#     print(s1-s2)
#
# elif calci== "*":
#     print(s1*s2)
#
# elif calci=="/":
#     print(s1/s2)
# else:
#     print("Invalid Oprations")

# car={
#       "parag":'123',
#       "rajat":'234',
#     "ram":'244'
# }
#
# cars=car.keys()
# print(cars)
# cp=car.items()
# print(cp)

# data ={"id": 12,
#     "email": "rachel.howell@reqres.in",
#         "first_name": "Rachel",
#         "last_name": "Howell",
#         "avatar": "https://reqres.in/img/faces/12-image.jpg",
#         "languages": ["java", "python"]}
#
# da=data["id"]
# print(da)
# d=data["first_name"]
# print(d)
# l=data["languages"][1]
# print(l)
# m=data.items()
# print(m)
# import json
# with open("D:\\Api data\EmployeeData.JSON") as car:
#     day=json.load(car)
#     print(type(day))
# with open("D:\\Api data\EmployeeData2.JSON") as cars:
#     day2=json.load(cars)
#
#     if day==day2:
#         print("files are same")
#     else:
#         print("data is nont same in files")
#
#         print(day)
#         print(day2)


# class Data():
#     def __init__(self, f, l):
#         self.f = f
#         self.l = l
#
#     def files(self):
#         # f = open("C:\\Users\parag.pande\Desktop\hello\parags.txt","r")
#         # print(f.read())
#
#         # l=open("C:\\Users\parag.pande\Desktop\hello\parag.txt","r")
#         # print(f.read())
#
#         if self.f.read() == self.l.read():
#             print("both files are same")
#
#
# obj = Data(open("C:\\Users\parag.pande\Desktop\hello\parags.txt", "r"),
#            open("C:\\Users\parag.pande\Desktop\hello\parag.txt", "r"))
# obj.files()

# import json
# import requests
#
# req = requests.get("http://216.10.245.166//Library/GetBook.php", params={"AuthorName": "Parag Pande"}
#                    )
# print(req.status_code)
# assert req.status_code == 200
#
# print(req.headers)
# print(req.headers["Content-Type"])
# assert req.headers["Content-Type"] == "application/json;charset=UTF-8"
#
# print(type(req))
#
# # parse in json
#
# py = json.loads(req.content)
# print(type(py))
# print(py)
#
# # validation of book
#
# for i in py:
#     i["book_name"] = "Learn with Parag"
#     print(i["isbn"])
#     assert i["isbn"] == "bczxdq"

# fruits = ("apple", "watermelon", "kiwi", "oranges", "apple")
# print(type(fruits))

# # index of fruits
# l = fruits.index("kiwi")
# print(l)
#
# # count the items in tuple
# m = fruits.count("apple")
# print(m)

# add some item in tuple then covert into list then print tuple
# list=list(fruits)
# print(type(list))
# list.insert(0,"mango")
# print(list)
#
# tuples=tuple(list)
# print(tuples)
# class Miss():
#     def __init__(self, a):
#         self.a = a
#
#     def no(self):
#         #a = [1, 2, 3, 4, 3, 7]
#         b = []
#         for i in self.a:
#             if i not in b:
#                 b.append(i)
#
#             else:
#                 print(i)
#
#
# obj = Miss([1, 2, 3, 4, 3, 7])
# obj.no()

