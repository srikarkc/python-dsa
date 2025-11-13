def isPalindrome(s):

    i, e = 0, len(s) - 1

    while i < e:
        if s[i] != s[e]:
            return False
        i += 1
        e -= 1
    
    return True

print(isPalindrome("heh"))

# The above solution doesn't skip non alpha-num chars


def is_alnum(c):
    return (
        'A' <= c <= 'Z' or
        'a' <= c <= 'z' or
        '0' <= c <= '9'
    )

def betterIsPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].is_alnum():
            l += 1

        while l < r and not s[r].is_alnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1

    return True