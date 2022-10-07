class Solution(object):
   def rotate(self, matrix):
      temp_matrix = []
      column = len(matrix)-1
      for column in range(len(matrix)):
         temp = []
         for row in range(len(matrix)-1,-1,-1):
            temp.append(matrix[row][column])
         temp_matrix.append(temp)
      for i in range(len(matrix)):
         for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
      return matrix

ob1 = Solution()
print(ob1.rotate([[1,5,7],[9,6,3],[2,1,3]]))
