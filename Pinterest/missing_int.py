### Given an array of integers, find the smallest missing integer. ###

def missing_int(array):
    index = 0
    while index < len(array):
        value = array[index]
        if value >= len(array):
            array[index] = -1
        else:
            swap = array[value]
            array[value] = value
            array[index] = swap
            value = swap
        if index == value or array[index] == -1:
            index += 1

    for x in xrange(len(array)):
        if array[x] == -1:
            return x
