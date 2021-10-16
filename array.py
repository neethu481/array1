from array import *
arr=array('i',[])
n = int(input("enter the length of the array"))

for i in range(n):
    x=int(input("enter the value"))
    arr.append(x)


print(arr)

val = int(input("enter the searched value"))

c=0
for a in arr:
    if a==val:
        print(c)
        break
    else:
        if a!=val:
            arr.append(val)


    c=c+1



