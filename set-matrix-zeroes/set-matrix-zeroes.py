class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_pos.append([i, j])
        
        for x, y in zero_pos:    
            for i in range(len(matrix)):
                matrix[i][y] = 0
            for i in range(len(matrix[0])):
                matrix[x][i] = 0