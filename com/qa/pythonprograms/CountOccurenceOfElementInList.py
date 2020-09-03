#input: list = [10,11,10,13,10,15,17,19,25]
#       x= 10
#output: 3  #10 appears 3 times in the list

#1. Using loop
list = [10,15,10,13,10,15,17,17,15,10]
x = 10
count = 0
for ele in list:
    if(ele == x):
        count = count+1
print("{} has occurred {} times".format(x,count))  #Formatted Output

print("****************************************")

#2. Using count() method
list2 = [10,15,10,13,10,15,17,17,15,10]
x = 15
print("{} has occurred {} times".format(x,list2.count(x)))  #Formatted Output

print("****************************************")

#3. Using Counter() method
from collections import Counter
list3 = [10,15,10,13,10,15,17,17,15,10]
x = 17
dict =Counter(list3)  #Will return dictionary with element:count format e.g. {10:4, 15:3, 13:1, 17:2}
print("{} has occurred {} times".format(x,dict[x])) #3

print("****************************************")