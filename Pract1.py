a = [1, 2, 3, 4, 5, 6, 7, 9, 10]
for i in range(1, 11):
    if i not in a:
        print(i)
    num = int(input("enter no"))
    if (num % 2) == 0:
        print("ebven no")
