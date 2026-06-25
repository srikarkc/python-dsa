class Solution:
    def contains_duplicate(self, nums):
        if not nums:
            return False
        
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)

        return False
    
    # one-line solution
    def contains_duplicate_one_line(self, nums):
        return len(nums) != len(set(nums))
    
import timeit
import random

solution = Solution()

# Test cases
no_duplicates = list(range(100000))          # worst case - no duplicates
early_duplicate = [1, 2, 1] + list(range(100000))  # best case - early duplicate
random_list = random.sample(range(200000), 100000)  # average case

test_cases = {
    "No duplicates (worst case)": no_duplicates,
    "Early duplicate (best case)": early_duplicate,
    "Random list (average case)": random_list,
}

RUNS = 100

for case_name, nums in test_cases.items():
    print(f"\n📋 {case_name}")

    t1 = timeit.timeit(lambda: solution.contains_duplicate(nums), number=RUNS)
    t2 = timeit.timeit(lambda: solution.contains_duplicate_one_line(nums), number=RUNS)

    print(f"  Loop solution:    {t1:.4f}s")
    print(f"  One-line solution:{t2:.4f}s")
    print(f"  Winner: {'Loop' if t1 < t2 else 'One-line'} by {abs(t1-t2):.4f}s")
