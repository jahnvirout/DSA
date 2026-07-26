class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_sub = 0
        for i in range(len(nums)):
            zero_count = 0
            for j in range(i,len(nums)):
                if nums[j] == 0:
                    zero_count += 1
                if zero_count > k:
                    break
                
                max_sub = max(max_sub,j-i + 1)
        return max_sub

        
        
            
                    