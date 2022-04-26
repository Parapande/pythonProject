'''arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]
missing_elements = []
for ele in range(arr[0], arr[-1]+ 1):
    if ele not in arr:
        missing_elements.append(ele)
print(missing_elements)'''
arr = [1, 2, 3, 4, 5, 7, 6, 9, 10]
missing_value = set(range(arr[0], arr[-1] + 1)) - set(arr)
print(missing_value)
