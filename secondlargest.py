def second_largest(s):
    if len(s) < 2:
        return "List must have at least 2 numbers."

    first = second = float('-inf')
    
    for num in s:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        return "No second largest number found (all numbers may be same)"
    return second

lst = input('Enter the list: ')
s = list(map(int, lst.split()))
print(f'Second largest number is: {second_largest(s)}')
