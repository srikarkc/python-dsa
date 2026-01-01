def remove_duplicates(array):
    if not array:
        return 0

    write = 1  # position to write next unique element
    for read in range(1, len(array)):
        if array[read] != array[read - 1]:
            array[write] = array[read]
            write += 1

    return write  # new length of unique portion


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")