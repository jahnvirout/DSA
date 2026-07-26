class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        for num in nums:
            count = 0
            for j in range(len(nums)):
                if num == nums[j]:
                    count +=1
               
            if count == 1:
                return num

                
            

