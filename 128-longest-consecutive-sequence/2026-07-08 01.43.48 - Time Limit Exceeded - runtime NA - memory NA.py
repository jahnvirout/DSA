class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            current = nums[i]
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

        return longest