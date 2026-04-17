class Solution:
    def group_anagrams(self, strs):
        if not strs:
            return []
        
        result_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            result_map.setdefault(sorted_word, []).append(word)

        return list(result_map.values())
