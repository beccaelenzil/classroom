def mystery(numbers, value):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high)//2
        if numbers[mid] > value:
            high = mid - 1
        elif numbers[mid] < value:
            low = mid + 1
        else:
            return mid
    
    
    if numbers[low] == value:
        return low
    
    return None

mystery([1,2,3,4,5,6,7,8,9,10], 10)



