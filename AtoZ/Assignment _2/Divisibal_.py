first = 1
last = 1000

for i in range(first, last):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i)
