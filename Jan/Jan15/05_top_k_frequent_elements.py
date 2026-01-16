from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        # max number of times a number can occur is the length of the list
        buckets = [[] for _ in range(len(nums) + 1)]

        # put the numbers in their respective position
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res