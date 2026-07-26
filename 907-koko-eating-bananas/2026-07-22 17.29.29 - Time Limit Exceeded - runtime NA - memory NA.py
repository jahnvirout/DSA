class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles)+1):
            hour = 0

            for pile in piles:
                hour += (pile+i-1)//i

            if hour<=h:
                return i
       