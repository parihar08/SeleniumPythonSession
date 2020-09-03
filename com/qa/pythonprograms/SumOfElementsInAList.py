#input: list = [10,20,30,40]
#output: 100

#1. Using loop with range()
list = [10,20,30,40]
total = 0
for i in range(0,len(list)):
    total = total+list[i]
print("List {} total is: {}".format(list,total))  #Formatted Output
print("------------------------------------------------------------")
print("Sum of elements in list",list,"is:",total)

print("************************************************************")

#2. Using sum() method
list1 = [10,20,30,40,50,60]
total1 = sum(list1)
print("List {} total is: {}".format(list1,total1))  #Formatted Output
print("------------------------------------------------------------")
print("Sum of elements in list",list1,"is:",total1)

print("************************************************************")