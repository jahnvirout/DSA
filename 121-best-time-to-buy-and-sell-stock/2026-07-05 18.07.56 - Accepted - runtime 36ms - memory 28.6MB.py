class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_price = nums[0]
        max_profit = 0

        for price in nums:
            if price < min_price:
                min_price = price

            profit = price - min_price
            max_profit = max(profit,max_profit)
        return max_profit
