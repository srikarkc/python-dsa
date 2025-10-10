def find_max_min(array):
    max, min = None, None

    for i in array:
        if min == None and max == None:
            min, max = i, i
        if i < min:
            min = i
        elif i > max:
            max = i

    return (max, min)