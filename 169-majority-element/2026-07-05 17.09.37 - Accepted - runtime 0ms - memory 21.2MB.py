class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #moores algo

        nums.sort()
        return nums[len(nums)//2]
