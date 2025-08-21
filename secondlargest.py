def second_largest(s):
    first = s[0]
    second = s[0]
    for num in s:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

lst=input('enter the list')
s=list(map(int,lst.split()))
print(f'second largest no is:{second_largest(s)}')