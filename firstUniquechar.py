def firstchar(s):
    countS = {}
    for ch in s:
        countS[ch] = countS.get(ch,0) + 1
    for i,c in enumerate(s):
        if countS[c]==1:
            return i
    return -1

s = input('enter the string:')
print(firstchar(s))