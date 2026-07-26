class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit = 0
        for i in range(len(nums)):
           for j in range(i+1, len(nums)):
              profit = nums[j] - nums[i]
              max_profit = max(max_profit,profit)
        
        return max_profit

