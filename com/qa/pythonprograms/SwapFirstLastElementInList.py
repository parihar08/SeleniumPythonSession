# Input: [12,35,9,56,24]
# Output: [24,35,9,56,12]

#1. Using temporary variable
list = [12,35,9,56,24]
print("List elements before swapping first and last elements",list)
print("--------------------------------------------------------------------------")
size = len(list)
temp = list[0]
list[0] = list[size-1]
list[size-1] = temp
print("List elements after swapping first and last elements",list)
print("--------------------------------------------------------------------------")

#2. Without using temporary variable
mylist = [22,45,54,14,88]
print("List elements before swapping first and last elements",mylist)
print("--------------------------------------------------------------------------")
mylist[0],mylist[-1] = mylist[-1],mylist[0]
print("List elements after swapping first and last elements",mylist)
print("--------------------------------------------------------------------------")

#3. Using Tuple Variable
list1 = [55,23,65,34,98]
print("List elements before swapping first and last elements",list1)
print("--------------------------------------------------------------------------")
get = (list1[-1],list1[0])  #Packing 98 and 55

list1[0],list1[-1] = get    #Unpacking
print("List elements after swapping first and last elements",list1)
print("--------------------------------------------------------------------------")

#4. Using * operand
list2 = [12,35,9,56,24]
print("List elements before swapping first and last elements",list2)
print("--------------------------------------------------------------------------")
start,*middle,end = list2
list2 = [end,*middle,start]
print("List elements after swapping first and last elements",list2)
print("--------------------------------------------------------------------------")

#5. Using pop method
list3 = [55,23,65,34,98]
print("List elements before swapping first and last elements",list3)
print("--------------------------------------------------------------------------")
first= list3.pop(0) #55
last= list3.pop(-1) #98
list3.insert(0,last)
list3.append(first)
print("List elements after swapping first and last elements",list3)
print("--------------------------------------------------------------------------")