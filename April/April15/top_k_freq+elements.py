class Solution:
    def top_k(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # The highest possible freq will be the length of the nums string
        # nums = [7,7,7,7] --> freq[4] = 7 so len(freq) should be (4+1) = 5
        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        result = []

        for f in range(len(freq) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result