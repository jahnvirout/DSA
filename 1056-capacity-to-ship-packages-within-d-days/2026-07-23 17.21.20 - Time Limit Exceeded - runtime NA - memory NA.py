class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        for capacity in range(low,high+1):
            days_used = 1
            current_weight = 0
            for weight in weights:
                if weight+current_weight <= capacity:
                    current_weight+=weight
                else:
                    days_used+=1
                    current_weight = weight
            if days_used<=days:
                return capacity