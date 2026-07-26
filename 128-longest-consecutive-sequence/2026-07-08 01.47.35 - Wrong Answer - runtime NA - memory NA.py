class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums)

        for i in range(len(set_nums)):
            current = nums[i]
            length = 1

            while current + 1 in set_nums:
                current += 1
                length += 1

            longest = max(longest, length)

        return longest