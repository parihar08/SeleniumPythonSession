#1. Without taking input from user using temporary variable

num1=10
num2=20

print("Value of Number1 before swapping: ",num1)
print("Value of Number2 before swapping: ",num2)
print("---------------------------------------")

temp = num1 #10
num1 = num2 #20
num2 = temp #10

print("Value of Number1 after swapping: ",num1)
print("Value of Number2 after swapping: ",num2)
print("---------------------------------------")


#2. Take input from the user using temporary variable

num3 = input("Enter Number3 Value: ")
num4 = input("Enter Number4 Value: ")

print("---------------------------------------")
print("Value of Number3 before swapping: ",num3)
print("Value of Number4 before swapping: ",num4)
print("---------------------------------------")

temp = num3
num3 = num4
num4 = temp

print("Value of Number3 after swapping: ",num3)
print("Value of Number4 after swapping: ",num4)
print("---------------------------------------")


#3. Without using temporary variable

num5 = input("Enter Number5 Value: ")
num6 = input("Enter Number6 Value: ")

print("---------------------------------------")
print("Value of Number5 before swapping: ",num5)
print("Value of Number6 before swapping: ",num6)
print("---------------------------------------")

num5,num6= num6,num5

print("Value of Number5 after swapping: ",num5)
print("Value of Number6 after swapping: ",num6)
print("---------------------------------------")