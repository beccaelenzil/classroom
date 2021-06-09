def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    n1 = len(list1)
    n2 = len(list2)
    iterate = True
    while iterate: 
        if i < n1 and j < n2 and list1[i] < list2[j]:
            merged_list.append(list1[i])
            i+=1
        elif j < n2:
            merged_list.append(list2[j])
            j+=1

        if i >= n1 and j >=n2:
            iterate = False


    return(merged_list)

print(merge([1,4,6,7],[-5,5,9,10]))

        