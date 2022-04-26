s1 = int(input("Enter Any Value="))
s2 = int(input("Enter Any Value="))
calculate = input("Enter What Operation want=")

if calculate == "+":
    print(s1 + s2)
elif calculate == "-":
    print(s1 - s2)
elif calculate == "*":
    print(s1 * s2)
elif calculate == "/":
    print(s1 / s2)
else:
    print("invalid operation")
