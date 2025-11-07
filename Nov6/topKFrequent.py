def topKFrequent(nums, k):
    count_map = {}

    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1

    sorted_items = sorted(count_map.items(), 
                         key= lambda x:x[1],
                         reverse=True)
    return [num for num, freq in sorted_items[:k]]