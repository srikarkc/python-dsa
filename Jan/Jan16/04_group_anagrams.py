class Solution:
    def groupAnagrams(self, strs):
        anagram_map = {}

        for w in strs:
            sorted_str = "".join(sorted(w))
            anagram_map.setdefault(sorted_str, []).append(w)

        return list(anagram_map.values())