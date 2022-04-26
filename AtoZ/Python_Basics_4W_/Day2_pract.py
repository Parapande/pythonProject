"""#string and casting

a="paraag" # a is assing to parag
print(a)

# multi line code print


c="parag pande"
print(c[2:6])
print(len(b))

# is present in

d="python is simple language"
print("iss" not in d)

e="python"
print(e[::])
# slice to end
print(e[1:])

f= "Hello, World!"
print(f.replace("H","P"))

g= "parag pande"
print(g.split(","))

h= ["1,2,3,5"]
rev=reversed
var = list(h) == list(rev)
print()

# duplicate item in find
def ram(x):
    return list(dict.fromkeys(x))
l=ram ([1,2,3,5,5,5,7,1])
print(l)
def numbers(x):
    return list(dict.fromkeys(x))

j=numbers(["a","b","c","b"])
print(j)
print(type(j))
a="james"
print(a[0:1]),print(a[2:3]),print(a[4:5])
str2 = "JaSonAy"
print(str2[2:5])
str1 = "Emma is a data scientist who knows Python. Emma works at google."
j=str1.find("mma")
print(j)


str12 = "12  1990 Emma is a 55 "
nums = "".join(items for items in str12 if items.isdigit())
print(nums)
a1=int(input("Enter a number "))
a2=int(input("Enter a number "))
calsi=input("opration to be taken=")
if calsi=="+":
    print(a1+a2)
elif calsi=="-":
    print(a1-a2)
else:
    print("invalid oprations")

l=["parag","ram","parag"]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i)"""
# import datetime
#
# a = "27/09/1997"
# b = "%d/%m/%Y"
# c = datetime.datetime.strptime(a, b)
# print(c)

# user= int(input("enter any no"))
# #2*1=2,2*2=4
#
# for i in range(1,11):
#     l=user*i
#     print(l)

# a=int(input("Enter any no\n"))
# if a % 2==0:
#     print("itd an even no")
# else:
#     print("its an odd no")

# s1 = int(input("enter any no"))
# s2 = int(input("enter any no"))
# calci = input("Any opration ")
#
# if calci == "+":
#     print(s1 + s2)
# elif calci == "-":
#     print(s1 - s2)
