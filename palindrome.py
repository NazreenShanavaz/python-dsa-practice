def alphaNum(c):
    return (
        'A' <= c <= 'Z' or 
        'a' <= c <= 'z' or 
        '0' <= c <= '9'
    )

def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        # Skip non-alphanumeric characters
        while l < r and not alphaNum(s[l]):
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1
        # Compare lowercase characters
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True



s = input("Enter a string: ")
if isPalindrome(s):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
