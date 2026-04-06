from collections import Counter

class Solution:
    def topKFreq(self, nums, k):
        count = Counter(nums)
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
                