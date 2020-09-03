#input: list = [3,2,4,7,8,19]
#output: smallest: 2    largest: 19

#1. Sort the list in ascending order and print first and last elements in the list
list = [3,2,4,7,8,19]
list.sort() #Sorting
print("Smallest element in list",list,"is:",list[0])
print("Largest element in list",list,"is:",list[len(list)-1])  #list[-1]

print("************************************************************")

#2. Min and Max methods
list1 = [3,2,4,7,8,19]
print("Smallest element in list",list1,"is:",min(list1))
print("Largest element in list",list1,"is:",max(list1))

print("************************************************************")