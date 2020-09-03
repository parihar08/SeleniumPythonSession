#input: madam
#output: Palindrome

#input: welcome
#output: Not Palindrome

# s = "abcde"
# print(s[:])     #abcde
# print(s[0:5])   #abcde
# print(s[0:5:1]) #abcde
# print(s[::])    #abcde
# print(s[::-1])  #edcba


input_string = input("Please enter a string: ")
reverse_string = (input_string[::-1])
if input_string == reverse_string:
    print(input_string,"is a Palindrome String")
else:
    print(input_string, "is not a Palindrome String")