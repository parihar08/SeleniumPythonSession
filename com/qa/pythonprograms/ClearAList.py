#input: list = [1,2,3,4,5,6]
#output: list = []

#1. Using clear() method
list = [1,2,3,4,5,6]
print("Original List",list)
print("****************************************")
list.clear()
print("List after clearing",list)
print("****************************************")

#2. Re-initialize list with no value
list1 = [1,2,3,4,5,6]
print("Original List",list1)
print("****************************************")
list1 = []
print("List after clearing",list1)
print("****************************************")

#3. Using "*=0" method removes all elements of the list and makes it empty
list2 = [1,2,3,4,5,6]
print("Original List",list2)
print("****************************************")
list2 *=0  #deletes the list
print("List after clearing",list2)
print("****************************************")

#4. Using del method
list3 = [1,2,3,4,5,6]
print("Original List",list3)
print("****************************************")
del list3[0:]   #del list3[:]
print("List after clearing",list3)
print("****************************************")