class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low<=high:
            mid = (low+high)//2
            hour = 0
            for pile in piles:
                hour += (pile+mid-1)//mid

            if hour <= h:
                high = mid -1
            elif hour > h:
                low = mid+1
        return low