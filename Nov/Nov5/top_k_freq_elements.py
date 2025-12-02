def topKfrequent(nums, k):
    num_map = {}

    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    sorted_items = sorted(num_map.items(), key = lambda x: x[1], reverse=True)

    return [num for num, freq in sorted_items[:k]]


# ChatGPT solution that is easy to read
def topKfrequent(nums, k):
    # Step 1: Count how often each number appears
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Sort the (number, frequency) pairs by frequency (high → low)
    sorted_pairs = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Take the first k numbers from the sorted list
    top_k = []
    for i in range(k):
        num, freq = sorted_pairs[i]
        top_k.append(num)

    return top_k
