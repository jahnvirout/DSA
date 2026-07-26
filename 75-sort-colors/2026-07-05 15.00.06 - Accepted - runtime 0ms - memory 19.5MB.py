class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0 = 0
        count_1 = 0
        count_2 = 0

        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1

        i = 0

        while count_0 > 0:
            nums[i] = 0
            i += 1
            count_0 -= 1

        while count_1 > 0:
            nums[i] = 1
            i += 1
            count_1 -= 1

        while count_2 > 0:
            nums[i] = 2
            i += 1
            count_2 -= 1