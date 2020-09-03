# Input: arr = [1,2,3]
# Max Output: 3
# Min Output: 1

arr = [23,17,67,39,20,87,22,47]

#Finding Max element
max = arr[0]
for i in range(1,len(arr)):
    if arr[i]> max:
        max =arr[i]
print("Maximum Value is:",max)

#Finding Min element
min = arr[0]
for i in range(1,len(arr)):
    if arr[i]< min:
        min =arr[i]
print("Minimum Value is:",min)