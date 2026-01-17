class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:

            # Skipping over the non alphanumeric characters

            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1

            # Evaluating whether it is a palindrome
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -=1 

        return True