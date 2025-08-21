def charector_freq(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq

s=input('enter the string:')

result = charector_freq(s)
print('charector frequencies:')
for char,count in result.items():
    print(f'{char}:{count}')