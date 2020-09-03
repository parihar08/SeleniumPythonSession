# input = ["geeks","for","geeks"]
# word = geeks, N=2
# output = ["geeks","for"]

list = ["geeks","for","geeks","is","my","list","geeks","geeks"]
word = "geeks"
n = 3 #which occurrence we want to remove
print("Original List Content is:",list)
count = 0
for i in range(0,len(list)-1):
    if(list[i] == word):
        count =count+1
        if(count==n):
            del list[i]
print("Updated List Content is:",list)