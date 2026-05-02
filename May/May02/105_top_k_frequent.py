class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        res = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                res.append(num)
                if len(res) == k:
                    return res
                    