def removeEl(num,val):
    k=0
    for i in range(len(num)):
        if num[i]!=val:
            num[k]=num[i]
            k+=1
    return k
    
num=list(map(int,input('enter the list:').split()))
val=int(input('enter the value to be removed:'))
print(removeEl(num,val))