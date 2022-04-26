# # # Python program to check if the number is an Armstrong number or not
# #
# # # take input from the user
# # num = int(input("Enter a number: "))
# #
# # # initialize sum
# # sum = 0
# #
# # # find the sum of the cube of each digit
# # temp = num
# # while temp > 0:
# #    digit = temp % 10
# #    sum += digit ** 3
# #    temp //= 10
# #
# # # display the result
# # if num == sum:
# #    print(num,"is an Armstrong number")
# # else:
# #    print(num,"is not an Armstrong number")
#
# num = int(input("Enter any no\n"))
#
# sum = 0
# temp = num
# while temp > 0:
#     no = temp % 10
#     sum += no ** 3
#     temp //= 10
# if sum == num:
#     print(num, "its an amstron")
# else:
#     print(num, "its no aramstronh")

# def param(fname):
#     print(fname,"pande")
#
# param("parag")
# param("nikhl")
# param("swapnil")
#
# def ram(lname,jname):
#     print(lname," ",jname)
#
# ram("pp","raj")

#
# def std(*names):
#     print("yongest std name is"+ names[2])
#
# std("rajat","raghav","deepak")
#
#
# def studesnts(ages):
#     print("The age of raman is " + ages)
#
#
# studesnts("23.90")
#
# import numpy
# def add(x,y):
#     sum=x+y
#     return sum
# num1=20
# num2=34
# print("sum of two Numberss",add(num2,num1))

# num is postive or negattive

# num=int(input("enter any no"))
#
# if num>0:
#     print("its an positve number")
# else:
#     print("its an negative number")

# local and global variable
#
# k="globel"
#
# def foo():
#     print("inside varible",k)
# # call inside functiin
# foo()
# #calling outside function
# print("its an gbobal variable",k)
#
# def joo():
#     x=23
#     print(x)
# joo()
#
# l=20
#
# def koo():
#     l=20
#     print(l)
# koo()

# local gbobal exp

# pp="global"
# def klp():
#     global pp
#     jj="local"
#     pp=[pp  *  3]
#     print(len(pp))
#     print(type(pp))
# klp()
# print(pp)

# year=int(input("eanter any year\n"))
#
# if year%4==0:
#     print("its leap year")
# else:
#     print("its not leap year")

p = [1, 23, 4, 6, 8, 90, 21, 6]
for i in p:
    if i * 2 == 0:
        print(i)

# def country(cot="india"):
#     print("i am from "+ cot)
#
# country("russia")
# country("japan")
# # taking default value
# country()
# country()
# country("usa")
#
# def func1(*args):
#     for i in args:
#         print(i)
#
# func1(20, 40, 60)
# func1(80, 100)

# Print range 4 to 30 with interval of 7
print(list(range(4, 30, 7)))

# print largest no in list

pl = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

print(max(pl))
print(min(pl))

for i in pl:
    if i % 2 == 0:
        print(i)

# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")