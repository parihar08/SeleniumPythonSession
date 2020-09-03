#Natural Number > 1
# Which has only 2 factors - 1 and itself

# 19 >=1 and 19 has no other factor => Hence 19 is prime number
# 28 >=1 but 2,4,7,14,28 are all factors => Hence 28 is not a prime number

num = int(input("Please enter the number: "))
count = 0
list= []

if num >1:
    for i in range(1,num+1):
        if(num%i) ==0:
            count = count+1
            list.append(i)
    if count == 2:
        print(num, "is Prime number")
        print(num, "is divisible by", count, "numbers:", list)
    else:
        print(num, "is not a Prime number")
        print(num, "is divisible by",count,"numbers:",list)
