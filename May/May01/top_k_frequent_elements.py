class Solution:
    def topKFreq(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        result = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                result.append(num)
                if len(result) == k:
                    return result