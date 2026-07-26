class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            if current_sum > nums[i]:
                current_sum = current_sum + nums[i]
            
            elif current_sum < nums[i]:
                current_sum = nums[i]

            max_sum = max(current_sum, max_sum)
        return max_sum
    
    