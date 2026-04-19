class Solution:
    def groupAnagrams(self, strs):
        res = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            res.setdefault(sorted_word, []).append(word)

        return res
    