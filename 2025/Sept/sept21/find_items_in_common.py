# Common interview questions to find items in common between 2 lists

# Method 1 - Inefficient (O(n^2))
def find_in_common_inefficient(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
            
    return False

# Method 2 - Efficient (O(n))
def find_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
        
    return False