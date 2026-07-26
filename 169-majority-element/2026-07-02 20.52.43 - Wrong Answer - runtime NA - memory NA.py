class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}  #key value pairs eg: 3 = key and 2 times apparead = value
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        if (count[num]) > len(nums) // 2:
            return num

        