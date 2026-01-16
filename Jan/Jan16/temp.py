strs = ["act","pots","tops","cat","stop","hat"]

anagram_map = {}

for w in strs:
    sorted_str = "".join(sorted(w))
    anagram_map.setdefault(sorted_str, []).append(w)
    print(anagram_map)

print(list(anagram_map.values()))