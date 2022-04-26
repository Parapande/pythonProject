a = ["parag", "paragpp", "raj", "pag", "parts"]
solve = """"t"
for i in a:
    if i[3:4]=="t":
        print(i)
        # This is a comment
        print("Hello, World!")
        x="rahul",2
        y= "promad",5
        if x<y:
            print("x is smaller")
        else:
            print("x is greater")

        j= "harry"
        m= 1
        c=1.3
        za=False
        print(type(j))
        print(type(za))
        print(type(c))
        print(type(m))
        # unpacking of collections mesns in 1st tubbple or list then next id list
        parag=[1,3,4]
        x,y,z=1,2,3
        print(x)
        print(y)
        print(z)
        print(x,y,z,parag)
        pp={"ram":"5"}
        pa={"ramji":"1"}
        print(pa,pp)
        
       
# local and global variables
smarts = " you are the best qa"


def staff():
    print("my name is parag" + smarts)


staff() 
# global variable
x = "is this clear"


def callthe_no():
    x = "is this clear"
    print("parag" + x)


def callagain():
    callthe_no()


print("ohh its good"+x)

a="ashis h"
j=a.replace(" ","ram")
print(j)

a=[1,3,6]
c=[1,3,6]
if a==c:
 print("yes both are same")
else:
    print("both are not same")

a = [1, 2, 3, 4, 7, 8]
for i in range(1, 9):
    if i not in a:
        print(i)"""
a = "parag"
l=a.split()
m=a.re
print(a)