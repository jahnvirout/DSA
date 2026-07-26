class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for key,value in dict.items():
            if value > n//2:
                return key

            