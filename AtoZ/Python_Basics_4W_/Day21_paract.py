# dam = {
#     12: "parag",
#     13: "ragav",
#     14: "amar",
#     15: "gavrav",
#     16: "swapnil"
# }
#
# print(dam[15])
# print(dam.items())
# for i in dam:
#    print(i)
#
# even odd
# a=int(input("enter no \n"))
# if a%2==0:
#     print("its an even on")
# else:
#     print("its an odd no")

# # multi
# user= int(input("enter no \n"))
# for i in range(1,11):
#    a=  user*i
#    print(a)


# a=int(input("enter any no"))
# b=[]
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)
#         b.append(i)
# if len(b)==2 or len(b)==1:
#     print("its an prime no")
# else:
#     print("not prime")

# a=["japan","janvey","india","germany","japny"]
#
# b=[x for x in a if "jap" in x]
# print(b)

# a=[21,22,24,25]
# for i in range(21,26):
#     if i not in a:
#         print(i)
#
# a=["a","b","c","a"]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         print(i)

# a=0
# b=1
# count=10
#
# for i in range(0,count):
#     sum=a+b
#     print(a)
#     a=b
#     b=sum
# class Ops():
#     def __init__(self,s1,s2,calci):
#         self.s1=s1
#         self.s2=s2
#         self.calci=calci
#     def cal (self):
#             # s1 = int(input("enter 1st no"))
#             # s2 = int(input("enter 1st no"))
#             #
#             # calci = input("enter 1st no")
#
#             if self.calci == "+":
#                 print(self.s1 + self.s2)
#             elif self.calci == "-":
#                 print(self.s1  - self.s2)
#             elif self.calci == "*":
#                 print(self.s1  * self.s2)
#             elif self.calci == "/":
#                 print(self.s1  / self.s2)
#
#             else:
#                 print("invalid oprations ")
# obj=Ops( int(input("enter 1st no")), int(input("enter 2st no")),input("enter oprator no"))
# obj.cal()
# import json
#
# import requests
#
# from AtoZ.Python_Basics_4W_.Utilities.Configration import getconfig
# from AtoZ.Python_Basics_4W_.Utilities.Resources import Resources
#
#
# def test_datas():
#
#     response = requests.get(getconfig()['API']['endpoint']+Resources.getbook,params={"AuthorName": "Rahul Shetty2"}, )
#     response_json = json.loads(response.content)
#     print(response_json)
# import xml.etree.ElementTree as Et
#
# with open("C:\\Users\parag.pande\Downloads\employee.xml") as data:
#  mytree=Et.parse(data)
#
#  print(type(mytree))
#  myroot=mytree.getroot()
#  print(myroot)

