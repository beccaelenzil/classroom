def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    rows = len(matrix)
    columns = len(matrix[0])

    if rows*columns != r*c:
        return matrix

    reshaped_matrix = []
    for i in range(r):
        new_row = []
        for j in range(i*columns, (i+1)*columns):
            new_row+=matrix[j]
        reshaped_matrix.append(new_row)
        
    return reshaped_matrix

print(reshape_matrix([[1,2],[3,4],[5,6],[7,8]],2,4))
print(reshape_matrix([[1,2],[3,4]],1,4))