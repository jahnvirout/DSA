class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for divisor in range(1, max(nums)+1):
            result = 0

            for num in nums:
                result += (num+divisor-1)//divisor

            if result<=threshold:
                return divisor