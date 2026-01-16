from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]

        for num, freq in count:
            buckets[freq].append(num)
            # we append because more than 1 number can have the same frequency
        
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res