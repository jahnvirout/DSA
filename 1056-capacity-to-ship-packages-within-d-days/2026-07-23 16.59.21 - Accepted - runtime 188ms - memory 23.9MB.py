class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low<=high:
            mid = (low+high)//2
            capacity = 0
            days_used = 1

            for num in weights:
                capacity += num

                if capacity > mid:
                    days_used+=1
                    capacity = num
            
            if days_used <= days:
                high = mid-1
            else:
                low = mid+1
        return low
