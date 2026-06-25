class Solution:
    def top_k_freq(nums, k):
        numCount = {}

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in numCount.items():
            freq[c].append(num)

        result = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                result.append(num)
                if len(result) == k:
                    return result
                