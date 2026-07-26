class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row = [0]*rows
        col = [0]*cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(rows):
            for j in range(cols):
                if row[i] == 1 or col[j]==1:
                    matrix[i][j] = 0
        return matrix



            