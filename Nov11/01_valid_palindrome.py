def alphaNum(c): 
    # Checks whether uppercase / lowercase / number
    return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

def isPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        # Move the l and r pointers to ensure that it is a valid character (ignore spaces / commas)
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1

        # Main logic
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    
    return True

