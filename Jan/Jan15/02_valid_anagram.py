class Solution:
    def valid_anagram(self, s, t):
        return sorted(s) == sorted(t)
    
    # The above solution works but sorting is O(nlogn) operation so time complexity for the above is O(nlogn)

    def valid_anagram_optimized(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
            
        return True
    
    # The above solution take O(n) time and O(n) space

    def valid_anagram_optimized_2(self, s, t):
        # This solution further optimized the space but only works if the problem uses lower case characters
        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
            if freq[ord(ch) - ord('a')] < 0:
                return False
            
        return True