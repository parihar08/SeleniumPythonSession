#input: list = [3,2,4]
#output: 24 #3*2*4=24

#1. Using Traversal approach
list = [3,2,4,5,6]
result = 1
for i in list:
    result = result*i
print("Multiplication of elements in list {} is: {}".format(list,result))  #Formatted Output
print("------------------------------------------------------------")
print("Multiplication of elements in list",list,"is:",result)

print("************************************************************")

#2. Using numpy.prod() * Install numpy package
import numpy
list1 = [3,2,4]
result1= numpy.prod(list1)
print("Multiplication of elements in list {} is: {}".format(list1,result1))  #Formatted Output
print("------------------------------------------------------------")
print("Multiplication of elements in list",list1,"is:",result1)

print("************************************************************")
