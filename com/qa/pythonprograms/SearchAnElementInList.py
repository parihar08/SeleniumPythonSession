# list =[1,2,3,4,5,6]
# element =4  --Element Found
# element =8  --Element Not Found

#1. Using Loop
list =[1,2,3,4,5,6]
ele = 5
flag=0
for i in list:
    if(i==ele):
        print("Element",ele,"Found")
        flag=1
        break
if(flag==0):
    print("Element", ele, "Not Found")

print("------------------------------------------")

#2. Using in operator
list1 =[1,2,3,4,5,6]
ele1 = 200
if(ele1 in list1):
    print("Element",ele1,"Found")
else:
    print("Element", ele1, "Not Found")