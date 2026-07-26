class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1

        while n>=row:
            n = n - row
            row +=1
        return row-1