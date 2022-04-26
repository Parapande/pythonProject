""""# fibo  serise

s = 0
s1 = 1
count = 10
for i in range(0, count):
    sum = s + s1
    print(s)
    s = s1
    s1 = sum

# pelendrom

road=input("enter ")
rev= reversed(road)
if list(road)==list(rev):
 print("its pelendrom")
else:
    print("not pelendrom")

# revserse string

stop="busstop stucks"
l=stop.split()
print(l)
l.reverse()
print(l)

# even odd

s1 = int(input("enter a number"))
if (s1 % 2) == 0:
    print("its an even number")
else:
    print("its an odd number")

#    prime number program

number = int(input("Enter any number: "))


if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

"""
#
a = 20
b = 30
print("previous values",a,b)
temp=a
a=b
b=temp

print("after swapping values are ",a)
print("after swapping values are",b)
