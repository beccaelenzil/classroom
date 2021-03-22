def sidewinder(number_list):
    # start at 0
    index = 0

    # keep going if value at current index != 0
    while number_list[index] != 0:

        #update index with value at current index
        index = number_list[index]

    # return index where the value = 0
    return index

def sidewinder(number_list):
    index = 0
    value = number_list[index]
    while value != 0:
        value = number_list[index]
        if value == 0:
            return index
        else:
            index = value

    return index

def sidewinder(number_list):
    index = 0
    while number_list[index] != 0:
        if number_list[index] != 0:
            index = number_list[index]
        else:
            return index

    return index



