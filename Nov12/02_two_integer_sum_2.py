# In this 2 sum problem - the provided array is sorted and you're not allowed to use the same number twice

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [numbers[left + 1], numbers[right + 1]]
        
        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []