class Solution:
    def top_k_freq(self, nums, k):
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count_map.items():
            freq[count] = num

        result = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                result.append(num)
                if len(result) == k:
                    return result
                