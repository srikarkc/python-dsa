from collections import defaultdict

def groupAnagrams(strs):
    str_map = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        str_map[key].append(word)

    return list(str_map.values())

strings = ["act","pots","tops","cat","stop","hat"]

groupAnagrams(strings)