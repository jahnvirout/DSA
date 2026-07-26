class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j] == nums[i]:
                    count+=1
        
        if count > n//2:
            return nums[i]
