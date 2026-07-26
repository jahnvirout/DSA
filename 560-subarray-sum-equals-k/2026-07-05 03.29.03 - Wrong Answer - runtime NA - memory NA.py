class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray = 0

        for i in range(len(nums)-1):
            if nums[i] +nums [i+1] == k:
                subarray+=1
            
        for i in range(len(nums)):
            if nums[i] == k:
                subarray+=1

        return subarray