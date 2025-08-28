from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)
    for words in strs:
        count = [0]*26
        for c in words:
            count[ord(c)-ord('a')]+=1
        res[tuple(count)].append(words)
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))