def maxval(s):
    maximum=s[0]
    for num in s:
        if num > maximum:
            maximum=num
    return maximum

lst=input('enter the list')
s=list(map(int,lst.split()))
print(maxval(s))