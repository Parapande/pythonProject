"""a = input("Enter 1st number\n")
b = input("Enter 2d number\n")
a = int(a)
print(type(a))
print(type(b))
b = int(b)
print("The sum of two numbers is",a+b)
c= int(input("enter an number"))
print(type(c))
print("sum of all three",a+b+c)


inpuut = float(input("enter number\n"))
reminder = inpuut % 7
print ("The reminder is",reminder)
a=34
b=22
b>a
print(b>a)
a=int(input("enter an no \n"))
b=int(input("enter an no\n"))
avg=(a+b)/2
print("avarage of two no",(a+b)/2)
m=int(input("enter any no"))
n=int(input("enter any no"))
add=print("add of two",m+n)
minus=print("sub of two",m-n)
multi=print("add of two",m*n)
div=print("add of two",m/n)"""
g = "global variable"


def massage():
    l = "local variable"
    print(l)
massage()
print(g)

