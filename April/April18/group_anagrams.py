from collections import defaultdict

class Solution:
    def group_anagrams(self, strs):
        res = defaultdict(list)

        for w in strs:
            sorted_word = "".join(sorted(w))
            res[sorted_word].append(w)

        return list(res.values())