class Solution:
    def valid_palindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
    