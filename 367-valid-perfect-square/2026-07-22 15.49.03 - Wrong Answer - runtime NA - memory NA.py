class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num):
            if i * i == num:
                return True
        return False