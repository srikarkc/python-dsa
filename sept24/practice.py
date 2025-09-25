def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1
            
            longest = max(longest, streak)

    return longest

print(longest_consecutive_sequence([1,2,3,100,200,300,400,5,4,68,69,65,64]))