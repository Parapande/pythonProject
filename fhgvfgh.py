#Take input from User

User= int(input("Enter a number"))
 #initializing Variables
First_Numb = 0
Second_Numb = 1
sum = 0
count = 1
print("fibonacci Series:",end='')
while(count<=User):
    print(sum,end='')
    count+=1
    First_Numb=Second_Numb
    Second_Numb = sum
    sum = First_Numb+Second_Numb
