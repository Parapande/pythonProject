'''details = {"parag": "donald", "ram":2, "aranav":1,}
for n in details:
    print(n)
for n in details.keys():
    print(n)
for n in details.values():
    print(n)'''
####################

arr = [1,2,3,7,9,10]
missing_value = set(range(arr[0],arr[-1])) -set(arr)
print(missing_value)
s1=[1,2,3,4,5,7]
miss=set(range(s1[0],s1[-1]))-set(s1)
print(miss)
