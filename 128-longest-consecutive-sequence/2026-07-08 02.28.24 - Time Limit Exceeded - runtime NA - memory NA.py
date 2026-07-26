class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       nums = set(nums)
       longest = 0

       for num in nums:

        if num-1 not in nums:
            current = num
            length = 1

            while current+1 in nums:
                length +=1
                current += num

            longest = max(length, longest)
        return longest



    


