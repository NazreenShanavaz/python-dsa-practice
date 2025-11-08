def replaceElement(arr,x,y):
    for i in range(len(arr)):
        if arr[i]==x:
            arr[i]=y
    return arr

arr=list(map(int,input('enter the list :').split()))
x=int(input('enter the number to be replaced:'))
y=int(input('enter the number to be replaced with:'))
print(replaceElement(arr,x,y))