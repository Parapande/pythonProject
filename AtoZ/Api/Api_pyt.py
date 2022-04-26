# import requests
# import json
# import jsonpath
# url ="https://reqres.in/api/users?page=2"
# responce=requests.get(url)
# print(responce)
#
#
# print(responce.content)
# print(responce.headers)
# jsonresponce=json.loads(responce.text)
# print(jsonresponce)
# p=jsonpath.jsonpath(jsonresponce,'total_pages')
# assert p[0]==2

# f= open("C:\\Users\parag.pande\Desktop\\api\\parags.txt","r")
# print(f.read())
# f.close()
# #for over ride
# f= open("C:\\Users\parag.pande\Desktop\\api\\parags.txt","w")
# print(f.write("parag pande "))

f=open("C:\\Users\parag.pande\Desktop\\api\\parags.txt","r")
for i in f:
    l=i.upper()
    print(l)
f.close()

