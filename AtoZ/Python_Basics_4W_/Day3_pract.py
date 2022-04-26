"""# ment to add ele at last
l = ["a", "v", "d"]
l.append("c")
print(l)

# add element to last postion
l.insert(1, "parag")
print(l)

# reverse menthod to string
l.reverse()
print(l)
for i in l:
    print(l)
# remove using index
l.pop(2)
print(l)

# Remove the element using name
l.remove("parag")
print(l)

# extend itesms
l.extend("paraggg")
print(l)

# copy method
l.copy()
print(l)

# sort the string
k = l.sort()
print(k)

# count mwrhod
l.count("paragy")
print(l)
"""  # Escape charater
# using \"parag\"
w = "parag is my name and i an in \"yash tech\""
print(w)
nums = "parag is my name and i am 25 year old \n and work at\"yash tech \n 6 month\"\n"
print(nums, w)
"""
# /r
mm = "pasnnndn \r mxmx"
print(mm)
# in list allowed duplicate and its changable
an = [1, 2, 3, 4, 5, 6, 2]
print(an[::])
print(len(an))

# join 3 strings and int and bool
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1 + list2 + list3)

# adding new to any index
fruits = ["apple", "parag", "mango", "kiwi"]
fruits[1] = "watermelone"
print(fruits)

#adding numbers to any postion giving index
nums = [1, 2, 3, 4, 5, 6, 8, 9,]
nums[8]=9000
print(nums)

#find missing no
nus = [1, 2, 3, 4, 5, 6, 8, 9,]
for i in range(1,10):
    if i not in nus:
        print(i)
#add item in list
ns = [1, 2, 3, 4, 5, 6, 8, 9,]
ns.insert(2,"mehul")
print(ns)

# last items add using append
ns.append("9272.90")
print(ns)

#reverse the list
ns.reverse()
print(ns)

ns.pop(0)
print(ns)

#add two list using extend method
no=[1,2,3,4,]
np=[8,6,3,4,]
no.extend(np)
print(no)

# for and if in lists

cont=["india","america","japan","indopak"]
connt=[x for x in cont if "jap" in x]
print(connt)

# sort using assending order
list1 = [12, 2, 3, 5, 4, 8, 7, 9]
for i in list1:
    if i % 2 == 0:
        print(i)

# list no interchngable 1 st and last
nx = [6, 33, 44, 4, 6, 67, 1]
nx[0],nx[-1]=nx[-1],nx[0]
print(nx)
"""
numss = ["parag", "tushar", "pa", "pat", "ram"]
num = [items for items in numss if "tu" in items]
print(num)
citys = ["AKOLA", "AMRAVATI", "PUNE", "MUMBAI", "NAGPUR"]
city = [i for i in citys if "PU" in i]
print(city)

npa=["parag", "tushar", "pa", "pat", "ramk"]
nc=[i for i in npa if "mk" in i]
print(nc)