class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        for i in range(len(nums)):
            length = 1
            current = nums[i]

            while current+1 in nums:
                current = current+1
                length = length+1

                longest = max(longest,length)
        return longest