class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       n = len(matrix)
       temp = [[0] * n for _ in range(n)]

       for i in range(n):
        for j in range(len(matrix[0])):
            temp[j][n-1-i] = matrix[i][j]

       for i in range(n):
        for j in range(len(matrix[0])):
            matrix[i][j] = temp[i][j]
       
       return matrix
    