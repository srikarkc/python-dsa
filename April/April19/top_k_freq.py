class Solution:
    def topKFrequent(self, nums, k):
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count_map.items():
            freq[count].append(num)

        res = []
        for f in range(len(freq) - 1, -1, -1):
            for num in freq[f]:
                res.append(num)
                if len(res) == k:
                    return res
