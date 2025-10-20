input_list_example = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagram_map(input_list):
    
    anagram_map = {}

    for word in input_list:

        key = ''.join(sorted(word))

        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)
    
    return list(anagram_map.values())