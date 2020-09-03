#input: "Welcome"
#output: 7

#1. Using for loop
str = input("Please enter a string: ")
print("************************************************************")
count = 0
for i in str:
    count = count+1
print("Length of String is:",count)
print("************************************************************")

#2. Using while loop and slicing technique
str1 = input("Please enter a string: ")
print("************************************************************")
count = 0
while str1[count:]:  #0:6  for Welcome
    count = count+1
print("Length of String is:",count)
print("************************************************************")

#3. Using length()
str2 = input("Please enter a string: ")
print("************************************************************")
print("Length of String is:",len(str2))
print("************************************************************")

#4. Using join and count
str3 = input("Please enter a string: ")  #welcome
print("************************************************************")
temp_str = "X"

print(temp_str.join(str3)) #wXeXlXcXoXmXe adding temporary 
print("Length of String is:",temp_str.join(str3).count(temp_str)+1) #7 Length of String
print("************************************************************")