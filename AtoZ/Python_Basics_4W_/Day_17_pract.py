# a = [2, 34, 5, 6, 8, 90, 34]
#
# a.insert(0,"34")
# a.append(2)
# print(a)
# print(a)

# x=20
# y=50
#
# x,y=y,x
# print(x,y)

# swapping from list

# a_list=[1,4,9]
#
# a_list[0],a_list[2]=a_list[2],a_list[0]
#
# print(a_list)

# by usig index

# b=[2,5,7,8,9]
#
# ind1=b.index(0)
# ind2=b.index(4)

# students = ["harry", "barry", "larry", "larry", "harry"]
# std = []
# for i in students:
#     if i not in std:
#         std.append(i)
#     else:
#         print(i)
#
# code = [20, 45, 4, 433, 2, 4]
# cd=[]
# for i in code:
#     if i not in cd:
#         cd.append(i)
#     else:
#         print(i)
# import json
#
# with open("D:\\Api data\EmployeeData.JSON") as datas:
#     dat = json.load(datas)
#     for i in dat:
#         # print(i)
#         print(i["id"]=="1006")
#

# class table():
#     def __init__(self,parag,swapnil):
#         self.parag = parag
#         self.swapnil = swapnil
#
#     def cal(self):
#         print("oh my god",self.parag)
#
# dj=  table("hello ","welcome")
# print(dj.parag)


# roll_no = [1, 23, 44, 55, 67, 22, 23, 45]
#
# for l in range(0, len(roll_no)):
#     for m in range(l+1,len(roll_no)):
#         if (roll_no[l]==roll_no[m]):
#             print(m)

#
# a=23
# b=36
# print(min(a,b))
# print(max(a,b))


# ap=[2,3,45,6,77,90]
#
# for i in ap:
#     if (i==3):
#         print(i)

# ap = [2, 3, 45, 6, 77, 90]
#
# kl = ap.clear()
# print(kl)

# a=[2,3,4,5,66]
# rev=reversed(a)
# print(list(rev))

# a=2
# b=3
# c=4
# print(a*b*c)
#
# user=int(input("Enter Any No \n"))
# if user%2==0:
#     print("its an even no")
# else:
#     print("its an odd no")
#
# pl = [34, 33, 4, 4, 67, 88, 2, 22]
# for i in pl:
#    print(i*2)

# class Dupli():
#     def dup(self,s1):
#         #s1 = ["parag", "harry", "barry", "harry"]
#         s2 = []
#
#         for i in s1:
#             if i not in s2:
#                 s2.append(i)
#             else:
#                 print(i)
#
#
#
# obj = Dupli()
# obj.dup(["parag", "harry", "barry", "harry"])

# class Miele:
#     def __init__(self, missing):
#         self.missing = missing
#
#     def miss(self):
#         # missing = [1, 2, 3, 4, 5, 7, 8, 9, 10]
#         for i in range(1, 11):
#             if i not in self.missing:
#                 print(i)
#
#
# obj = Miele([1, 2, 3, 4, 5, 7, 8, 9, 10])
# obj.miss()


# prime no 6 =1 ,2 3 6 if 3 = 3 ,1

# sum=int(input("Enter no \n"))
# s1=[]
# for i in range(1,sum+1):
#     if i not in s1:
#         s1.append(i)
# if len(s1)==2 or len(s1)==1:
#     print("its prime no")
# else:
#     print("its not prime no")
class Prime():
    def __init__(self,a):
        self.a=a
    def primeno(self):
        #a=int(input("enter any no"))
        b=[]
        for i in range(1,self.a+1):
            if self.a%i==0:
                b.append(i)
                print(i)
        if len(b)==2 or len(b)==1:
            print("its an prme no")
        else:
            print("not prime no")

obj=Prime(49)
obj.primeno()