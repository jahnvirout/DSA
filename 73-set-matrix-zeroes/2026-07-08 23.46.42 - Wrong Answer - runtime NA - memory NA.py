class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # First pass: mark cells with -1
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:

                    # Mark the column
                    for r in range(rows):
                        if matrix[r][j] != 0:
                            matrix[r][j] = -1

                    # Mark the row
                    for c in range(cols):
                        if matrix[i][c] != 0:
                            matrix[i][c] = -1

        # Second pass: convert -1 to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
            