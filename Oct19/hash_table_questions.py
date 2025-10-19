# Question 1 - return true if there's at least 1 item in common between 2 lists

def item_in_common(list1, list2):
    my_dict = {}

    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
        
    return False

# Here's an even more Pythonic way of doing the above problem
def is_item_in_common(list1, list2):
    return bool(set(list1) & set(list2))


# Question 2  - Given an array of integers (nums), find all the duplicates in the array using hash table

def find_duplicates(input_list):
    output_array = []
    my_dict = {}
    for i in input_list:
        if i in my_dict:
            output_array.append(i)
        else:
            my_dict[i] = True
    return output_array


# Question 3 - Find the first non-repeating character

def first_non_repeating_char(input_string):

    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1