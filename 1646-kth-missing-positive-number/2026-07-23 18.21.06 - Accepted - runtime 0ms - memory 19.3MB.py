class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)-1
        x=0

        while low<=high:
            mid = (low+high)//2

            missing = arr[mid] - (mid+1)

            if missing < k:
                low = mid+1
            else:
                high = mid - 1
            
            missing_high = arr[high]- (high+1)
            x = k - missing_high
            ans = arr[high]+x
        return ans
