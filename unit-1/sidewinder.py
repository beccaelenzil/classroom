def sidewinder(number_list):

    # returns None for an empty array
    if len(number_list) == 0:
        return None
    
    # start at index 0
    index = 0

    # initialize indices that have been visited
    visited = [index]
    
    # evaluate the value of the list at the index and check if it equals 0
    while number_list[index] != 0:

        # check if we've already been there
        if number_list[index] in visited:
            # we're in an infinite sidewinder
            return "infinite"
        else:
            # if it doesn't equal 0 keep going and assign the value at that index as the new index
            index = number_list[index]

            # append that index to places that have been visited
            visited.append(index)

    #print(visited)

    # if we've visited all spots
    if len(number_list) == len(visited):
        return True
    #otherwise
    else:
        return False

    
print("sidewinder([]) returns",sidewinder([]))
print("sidewinder([2, 0, 1, 3]) returns",sidewinder([2, 0, 1, 3]))
print("sidewinder([2, 0, 1]) returns",sidewinder([2, 0, 1]))
print("sidewinder([1, 2, 1]) returns",sidewinder([1,2,1]))