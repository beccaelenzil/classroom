def kth_missing_positive_number(numbers, k):
    '''
    INPUT: List of numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    '''

    # n = len(numbers)
    # count = 0
    
    # for i in range(1,n+k+1):
    #     if i not in numbers and count < k:
    #         num = i
    #         count += 1
    # return num

    i = 0
    count = 0
    
    while count < k:
        if i not in numbers:
            count += 1

        i+=1

    print(i)
    return i

kth_missing_positive_number([1,2,3,4],2)
kth_missing_positive_number([2,3,4,7,11],6)
kth_missing_positive_number([2,3,4,7,11],5)