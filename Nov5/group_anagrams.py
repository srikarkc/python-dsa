def group_anagrams(strs):
    anagram_map = {}

    for s in strs:
        sorted_string = "".join(sorted(s))
        anagram_map.setdefault(sorted_string, []).append(s)

    return list(anagram_map.values())