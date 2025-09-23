def common_items(list1, list2):
    item_dict = {}

    for i in list1:
        item_dict[i] = True

    for j in list2:
        if j in item_dict.keys():
            return True
    
    return False


def find_duplicates(my_int_array):
    is_dup = {}

    for i in my_int_array:
        if i not in is_dup.keys():
            is_dup[i] = False
        elif i in is_dup.keys():
            is_dup[i] = True
        else:
            print("Unknown error occured")
            return
        
    output_array = []
    for key, value in is_dup.items():
        if value == True:
            output_array.append(key)

    return output_array


def first_non_repeating_char(input_string):
    char_count = {}

    for ch in input_string:
        char_count[ch] = char_count.get(ch, 0) + 1

    for ch in input_string:
        if char_count[ch] == 1:
            return ch
        
    return None

