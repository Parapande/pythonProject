'''s1 = int(input("enter frist no"))
s2 = int(input("enter second no"))
calci = input("oprations of numbers=")
if calci == "+":
    print(s1 + s2)
elif calci == "-":
    print(s1 - s2)
elif calci == "*":
    print(s1 * s2)
elif calci == "/":
    print(s1 / s2)
else:
    print("invalid orations")
a = 0
b = 1
# we have set the range
count = 10
for i in range(0, count):
    c = a + b
    print(a)
    a = b
    b = c                '''
citylist = ["India", "japan", "Indoneshia"]
j=citylist.pop(1)
print(j)
sub2="jap"
for i in citylist:
    if i[0:3]:
        print(i)