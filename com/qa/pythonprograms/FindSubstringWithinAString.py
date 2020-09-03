#input: "Welcome to Python Programming"
#substring: "Python"

#find() method finds the first occurrence of the specified value and returns the position
#find() method returns -1 if the value is not found

input_string = input("Please enter a string: ")
print("************************************************************")
print("Original string is:",input_string)
print("************************************************************")

sub_string="Python"

print(input_string.find(sub_string)) #11
print("************************************************************")

if(input_string.find(sub_string)== -1):
    print(sub_string,"Not Found")
else:
    print(sub_string,"Found")
