# import json
# import requests
#
# from AtoZ.Python_Basics_4W_.Day11_post_data_04 import load_post_data
#
# parag = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Parag Pande"})
#
# print(parag.status_code)
# print(parag.headers)
#
# print(parag.headers["Server"])
# print(parag.headers["Content-Type"])
# assert parag.status_code == 200
#
# da = json.loads(parag.content)
# print(da)
# for i in da:
#     if i["isbn"] == "bczxdx":
#         print(i)
#
# para = requests.post("http://216.10.245.166/Library/Addbook.php",
#                      json=load_post_data())
# print(para.status_code)
#
# print(para.headers)
# print(para.headers["Server"])
#
# pd = json.loads(para.content)
# print(pd)
#
# for i in pd:
#     if i["Msg"] == "successfully added":
#         print(i)


# global variable

# x="traing is on going"
# def pract():
#     print("my",x)
# pract()

# import random
#
# for i in range(1, 10):
#     print(random.randrange(i))

# a="Python training is on going "
# l=a.replace("Py","ja")
# print(l)
#
# m=a.upper()
# print(m)
#
# n=a.lower()
# print(n)
#
# o=a.casefold()
# print(o)
#
# p=a.count("o")
# print(p)
#
# q=a.split()
# print(q)
# print(type(q))

#
# lists = [90, 23, 3, 4, 4, 4, 4, 2, 2, 2, 3, 5, 7, 8, 8]
# list = []
# for i in lists:
#     if i not in list:
#         list.append(i)
#     else:
#         print(i)

# Write a program to accept a string and display it in upper case.

# str=input("Enter any String :")
# print(str.upper())

# Write a program to accept a string and display the ascii value of each character.
# a = input("Enter any String :")
# for i in a:
#     print("ascii value of", i, "is", ord(i))

# Write a program to accept a string and replace all spaces by ‘#’ symbol.
#
# str="parag pande"
# p=str.replace(" ","#")
# print(p)

# Write a program to accept two strings from the user and display the common words.(Ignore case)

# st1=input("Enter any string")
#
# st2=input("Enter any string")
#
# for i in st1:
#     if i in st2:
#         print(i)

#Write a program to accept a string and count the frequency of each vowel.

# st=input("Enter any thing")
#
# print(st.count("a"))
# print(st.count("e"))
# print(st.count("i"))
# print(st.count("o"))
# print(st.count("u"))

#Write a program to accept a string and display the string in Title case. (first alphabet of each word in upper case)

# sts=input("enter any string")
#
# print(sts.title())
#
# print(sts.swapcase())

# k="hello"
# print(k[2:4])
# print(k[:-1])

# user=input("reverse any stings")
# rev=reversed(user)
# if list(user)==list(rev):
#     print("its an plendrom")
# else:
#     print("its no pelndrom!")

# swapping of two strings
# a="xy"
# b="cd"
#
# print("befor print",a,b)
#
# temp=a
# a=b
# b=temp
# print(a,b)
#

