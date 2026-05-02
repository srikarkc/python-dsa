class Solution:
    def groupAnagrams(self, strs):
        anagram_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map.setdefault(sorted_word, []).append(word)

        return list(anagram_map.values())