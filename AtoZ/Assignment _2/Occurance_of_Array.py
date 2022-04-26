# list=[1,3,9,3,3]
# list=[1,3,3]
list = [1, 2, 3]
a = 3
count = 0
for ele in list:
    if (ele == a):
        count = count + 1
        print("{} occurred {} times ".format(a, count))
