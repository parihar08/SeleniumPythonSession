# Input: [12,35,9,56,24]  Swap pos1 & pos3
# Output: [12,56,9,35,24]

#1. Simple Swap - Swap position with index 1 and 3
list = [12,35,9,56,24]
print("List elements before swapping",list)
print("--------------------------------------------------------------------------")
pos1,pos3=1,3
list[pos1],list[pos3]=list[pos3],list[pos1]
print("List elements after swapping",list)
print("--------------------------------------------------------------------------")

#2. Using pop function - Swap position with index 2 and 4
list1 = [12,35,9,56,24]
print("List elements before swapping",list1)
print("--------------------------------------------------------------------------")
pos2,pos4=2,4
second_element=list1.pop(pos2) #9
fourth_element=list1.pop(pos4-1) #24 -Since we have already popped out one element in last step

list1.insert(pos2,fourth_element)
list1.insert(pos4,second_element)
print("List elements after swapping",list1)
print("--------------------------------------------------------------------------")

#3. Using Tuple variable - Swap position with index 1 and 3
list2 = [12,35,9,56,24]
print("List elements before swapping",list2)
print("--------------------------------------------------------------------------")
pos1,pos3=1,3

get = (list2[pos1],list2[pos3])
(list2[pos3],list2[pos1]) = get
print("List elements after swapping",list2)
print("--------------------------------------------------------------------------")