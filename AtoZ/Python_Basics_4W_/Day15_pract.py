# num = int(input("enter any no"))
# sum = 0
# # 153 1*3times+
# temp = num
# while temp > 0:
#     no = temp % 10
#     sum += no ** 3
#     temp//= 10
# if sum == num:
#     print("its an armastonh")
# else:
#
#     print("itds not")

# pl = (tuple(range(50, 100, 5)))
# for i in pl:
#     if i % 2 == 0:
#         print(i)
#         if i==50:
#             break

# 3 x 2 x 1 = 6.
# num= int(input("Enter any No\n"))
# sum=0
#
# for i in range(1,num+1):
#     sum=i*sum
#     print(i)
# if num==sum:
#     print(num,"its an factorail")
#
# else:
#     print(num,"not factorial no")
# multiply=1
# a = int(input("enter the num\n"))
# for i in range(1,a+1):
#     multiply = multiply * i
# print(a,multiply)

# 4*3*2*1=24
# muti=1
# a=int(input("enter any no"))
# for i in range(1,a+1):
#     muti=muti*i
# print(muti)

# a=[1,2,4,5]
# for i in range(1,6):
#    if  i not in a:
#        print(i)

# a=[1,2,3,4,"apple","apple",4]
# p=[]
# for i in a:
#     if i not in p:
#         p.append(i)
#     else:
#         print(i)
#
# citys=["pune","akola","jaipur","punes","purdek"]
# city=[i for i in citys if "pun" in i]
# print(city)

# a="pune junction"
# # for i in a:
# #     print(i)
# l=a.replace(" ","akola")
# print(l)

# import datetime
# a=datetime.datetime.now()
# print(a)
# print(a.year)
# print(a.strftime("%A"))

# import datetime
# d=datetime.datetime(2107,8,9)
# print(d)

# a = [2, 3, 4, 5, 6, 7]
# print(max(a))
# print(min(a))
# print(list(range(4,6,1)))
# for i in a:
#   print(i*2)
#
# import math
# # armastong 3!= 3*3+
# a=pow(1,3)
# b=pow(5,3)
# c=pow(3,3)
# print(a+b+c)
#
# m=64
# x=math.sqrt(m)
# print(x)

# class Person():
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city
#     def myself(self):
#         print("my name is",self.name)
# p1=Person("parag","25","pune")
# print(p1.name,p1.age,p1.city)

class students():
    def __init__(self, name, qulification, percentages, result):
        self.name = name
        self.qulification = qulification
        self.percentages = percentages
        self.result = result

    def candidates(self):
        print("hello my name is ", self.name)


po = students("parag", "B.Engineering", "7.5", "pass")
print(po.name, )
print(po.percentages)
print(po.qulification)
print(po.result)

a = [2, 34, "parag", 78]
# itreation without lopping
k = iter(a)
print(next(k))
print((next(k)))
print((next(k)))
print((next(k)))

from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())
print("year=", a.year)
