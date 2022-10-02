
def diagonalDifference(arr):
    right_dia_sum = 0   
    left_dia_sum = 0
    for i in range(len(arr)):
        #right traversing diagonal elements have the same row and column as index
        right_dia_sum += arr[i][i]    
        # left traversing diagonal elements will have their row number increasing and column number decreaseing or vice-versa
        left_dia_sum += arr[i][(len(arr)-1)-i]
    return abs(left_dia_sum - right_dia_sum)
