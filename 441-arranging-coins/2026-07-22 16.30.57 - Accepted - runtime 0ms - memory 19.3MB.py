class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n

        while low<=high:
            mid = (low+high) // 2
            coins_needed = (mid * (mid+1))//2

            if n == coins_needed:
                return mid
            elif n < coins_needed:
                high = mid - 1
            else:
                low = mid + 1
        return high
