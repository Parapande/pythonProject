'''s1=int(input("Enter 1st no"))
s2=int(input("enter second no"))
calci=input("opration we want")

if calci=="+":
    print(s1+s2)
elif calci=="-":
    print(s1-s2)
elif calci=="*":
    print(s1*s2)
elif calci=="/":
    print(s1/s2)
else:
    print("invalid opration")
user = (input("ender a no"))
rev = reversed(user)
if list(user) == list(rev):
    print("its a palendrom")
else:
    print("not pelendrom")'''
n1 = 0
n2 = 1
count = 10
for i in range(0, count):
    n3 = n1 + n2
    print(n1)
    n1 = n2
    n2 = n3
