#input: list = [10,11,12,13,14,15]
#output: list_copy = [10,11,12,13,14,15]

#1. Using slicing technique
list1 = [10,11,12,13,14,15]
print("Original List1",list1)
print("****************************************")
list1_copy = list1[:]
print("Cloned List1",list1_copy)
print("****************************************")

#2. Using extend() method
list2 = [10,11,12,13,14,15]
print("Original List2",list2)
print("****************************************")
list2_copy = []
list2_copy.extend(list2)
print("Cloned List2",list2_copy)
print("****************************************")

#3. Using list() method
list3 = [10,11,12,13,14,15]
print("Original List3",list3)
print("****************************************")
list3_copy = list(list3)
print("Cloned List3",list3_copy)
print("****************************************")

#4. Using copy() method
list4 = [10,11,12,13,14,15]
print("Original List4",list4)
print("****************************************")
list4_copy = list4.copy()
print("Cloned List4",list4_copy)
print("****************************************")

#5. Using list comprehension
list5 = [10,11,12,13,14,15]
print("Original List5",list5)
print("****************************************")
list5_copy = [i for i in list5]
print("Cloned List5",list5_copy)
print("****************************************")