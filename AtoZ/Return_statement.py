# factorials 4=4*3*2*1=24
#
# a = int(input("enter anu no\n"))
# multis = 1
# for i in range(1, a+1):
#     multis = multis * i
# print(multis)
# perfect number 6= 1+2+3 28=
# user=int(input("Enter any number\n"))
# sum=0
#
# for i in range(1,user):
#     if user%i==0:
#         sum=sum+i
#
# if user==sum:
#     print("perfect number")
# else:
#     print("not perfect number")


# 0 1 1
# a = 0
# b = 1
# print(a)
# print(b)
#
# for i in range(2,11 ):
#     sum = a + b
#
#     a = b
#     b = sum
#     print(sum)
# a=90
# b=30
#
# a,b=b,a
# print(a,"value of a is")
# print(b,"value of b is")

# perfect no 6=1+2+3=6
# a = int(input("Enter any no\n"))
#
# sum = 0
# for i in range(1, a):
#     if a % i == 0:
#         sum = sum + i
# print(sum)
# if sum==a:
#     print("its an perfect no")
# else:
#     print("its not perfect")


for i in range(1,6):
    for j in range(5,0,-1):
        if (i==j):
            print("*",end="")
        else:
            print(j,end="")