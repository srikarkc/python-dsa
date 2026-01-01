def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        # The second part j > -1 is for the first 2 elements being swapped.
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list