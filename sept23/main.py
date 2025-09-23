def group_anagrams(strings):
    anagram_map = {}

    for word in strings:
        key = ''.join(sorted(word))

        if key not in anagram_map.keys():
            anagram_map[key] = []

        anagram_map[key].append(word)

    return list(anagram_map.values())

# print(group_anagrams(['eat', 'tan', 'tea', 'ant', 'bat']))


# Problem 2 - Two sums
def two_sums(nums, target):
    my_dict = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in my_dict:
            return [my_dict[difference], i]
        my_dict[num] = i

    return []

def subarray_sums(nums, target):
    sum_index = {0, -1}
    sum = 0

    for i, num in enumerate(nums):
        sum += num

        if (target - sum) in sum_index:
            return [sum_index[target - sum] + 1, i]
        
        sum_index[sum] = i
    return []