#input: "Welcome to Python Programming"
#output: "Programming Python to Welcome"

input_string = input("Please enter a string: ")
print("************************************************************")
print("Original string is:",input_string)
print("************************************************************")

words = input_string.split(" ")
print("Splitted list is:",words) #['Welcome', 'to', 'Python', 'Programming']
print("************************************************************")

words=words[-1::-1]
print("Reverse Splitted list is:",words) #['Programming', 'Python', 'to', 'Welcome']
print("************************************************************")

reversed_string = ' '.join(words)
print("Reversed string is:",reversed_string)  #Programming Python to Welcome
print("************************************************************")
