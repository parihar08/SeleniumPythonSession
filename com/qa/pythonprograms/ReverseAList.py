#input: list = [10,11,12,13,14,15]
#output: list = [15,14,13,12,11,10]

#1. Using Reverse List method
list = [10,11,12,13,14,15]
print("Original List",list)
print("****************************************")
list.reverse()
print("List after reversing",list)
print("****************************************")


#2. Using slicing technique
list1 = [10,11,12,13,14,15]
print("Original List",list1)
print("****************************************")
list2 = list1[::-1] #list1[start:end:step]
print("List after reversing",list2)
print("****************************************")