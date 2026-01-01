# Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.

# The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.

def remove_element(nums, val):
    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1