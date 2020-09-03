#input: list = [3,2,4,7,8,19]
#output: second_largest: 8

#1. Sort the list in ascending order and print second largest element in the list
list = [3,2,4,7,8,19]
list.sort() #Sorting
print("Largest element in list",list,"is:",list[-1])
print("Second Largest element in list",list,"is:",list[-2])

print("************************************************************")

#2. Remove the largest element

list1 = [3,2,4,7,8,19]
print("Largest element in list",list1,"is:",list1[-1])
list2 = set(list1) #Converts the list to a set
list2.remove(max(list2))  #Removes the largest element from the set
print("Second Largest element in list",list1,"is:",max(list2)) #Second largest element is now the largest
