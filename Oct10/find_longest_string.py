def find_longest_string(array):
    longest_string = ''
    
    for i in range(len(array)):
        if longest_string == None:
            longest_string = array[i]
        elif len(array[i]) > len(longest_string):
            longest_string = array[i]
            
    return longest_string


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  