# Problem 1 - remove duplicate values from a list

def remove_duplicates(input_array):
    my_set = set()
    for i in input_array:
        my_set.add(i)
    return my_set


# Problem 2 - takes an input string and finds if all the characters are unique

def has_uniques_chars(input_string):
    char_set = set()

    for char in input_string:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    
    return True


# Problem 3 - Find pairs totalling to target
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []

    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))

    return pairs


# Problem 4 - Longest consecutive sequence
def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                streak += 1
                current += 1

        longest = max(streak, current)
    
    return longest