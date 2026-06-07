# Search in rotated sorted array problem

Even though the array is rotated - one 1/2 is always sorted. 

First, Figure out whether this is the left half or the right half.

Second, figure out whether the target falls within this range.

For the first part, if `nums[mid] <= nums[left]`, this means that the first half is sorted.

Note that in this problem, the condition for the loop is `left <= right`.
