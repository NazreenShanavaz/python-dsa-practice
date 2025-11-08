def mergeSortArray(num1,num2,m,n):
    last=m+n-1
    n-=1
    m-=1
    while m>0 and n>0:
        if num1[m]>num2[n]:
            num1[last]=num1[m]
            m-=1
        else:
            num1[last]=num2[n]
            n-=1
        last-=1
    while n>0:
        num1[last]=num2[n]
        n-=1
        last-=1
    return num1

num1=list(map(int,input('enter the list1').split()))
num2=list(map(int,input('enter the list2').split()))
m=int(input('enter the valid number of num1'))
n=len(num2)
print("Merged Array:",mergeSortArray(num1,num2,m,n))
