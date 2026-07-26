import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for divisor in range(1, len(nums)+1):
            result = 0

            for num in nums:
                result += (result+num-1)/num

            if result<=threshold:
                return num