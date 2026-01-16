from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        def isAnagram(a, b):
            return sorted(a) == sorted(b)
        
        output_list = []
        used = set()

        for i in range(len(strs)):
            if i in used:
                continue

            cur_list = strs[i]
            used.add(i)

            for j in range(i + 1, len(strs)):
                if j in used:
                    continue
                if isAnagram(strs[i], strs[j]):
                    cur_list.append(strs[j])
                    used.add(j)

            output_list.append(cur_list)

        return output_list
    
    def groupAnagrams_optimized(self, strs):
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)

        return list(groups.values())