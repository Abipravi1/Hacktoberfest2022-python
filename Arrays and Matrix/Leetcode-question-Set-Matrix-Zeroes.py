def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        row=[] #need to store the indeces of rows which will be equal to 0
        col=[] #need to store the indeces of columns which will be equal to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i) #storing the indeces of rows
                    col.append(j) #storing the indeces of columns
                    
        #need to skip the duplicates to restict the TLE
        row=set(row) 
        col=set(col) 
        for i in range(len(matrix)): #for rows indeces
            if i in row: 
                matrix[i]=[0]*len(matrix[0]) #update the whole row to 0 (total columns in particular row = len(matrix[0])) 
            for j in range(len(matrix[0])): #for columns indeces
                if j in col:
                    matrix[i][j]=0 #updating the whole column to 0 one by one
        
