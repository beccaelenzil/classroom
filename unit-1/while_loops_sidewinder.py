def sidewinder(number_list):
    #guard clause
    if len(number_list) == 0:
        return None
    # elif 0 not in number_list:
    #     return None

    # start at 0
    index = 0
    visited = [index]

    # keep going if value at current index != 0
    while number_list[index] != 0:

        #update index with value at current index
        index = number_list[index]
        if index in visited:   
            return "infinite"

        visited.append(index)

    if len(visited) == len(number_list):
        return True
    else:
        return False

print("sidewinder([]) returns",sidewinder([]))
print("sidewinder([2, 0, 1, 3]) returns",sidewinder([2, 0, 1, 3]))
print("sidewinder([2, 0, 1]) returns",sidewinder([2, 0, 1]))
print("sidewinder([1, 2, 1]) returns",sidewinder([1,2,1]))





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



