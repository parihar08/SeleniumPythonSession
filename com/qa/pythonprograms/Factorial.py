#Factorial of 5: 5*4*3*2*1 = 120

#1. Iterative approach

num = int(input("Please enter the number for iterative approach: "))
factorial = 1

if num <0:
    print("Factorial doesn't exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("Factorial of",num,"is:",factorial)

#2. Recursive approach

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

num1= int(input("Please enter the number for recursive approach: "))
print("Factorial of",num1,"is:",factorial(num1))


#3. Recursive approach using Ternary operator for writing in one statement

def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)

num1= int(input("Please enter the number for recursive approach using Ternary operator: "))
print("Factorial of",num1,"is:",factorial(num1))
