from collections import defaultdict

def isValidSudoku(board):
    mat2 = {0:'0',1:'0',2:'0',3:'1',4:'1',5:'1',6:'2',7:'2',8:'2'}
    
    cheC = defaultdict(set)
    che = defaultdict(set)
    for i in range(9):
        temps = set()
        for j in range(9):
            num = board[i][j]
            
            if num != '.':
                if num  in temps:
                    return False
                temps.add(num)
                box = mat2[i]+mat2[j]
                if num in che[box]:
                    return False
                che[box].add(num)
                if num in cheC[j]:
                    return False
                cheC[j].add(num)
                    
    
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))