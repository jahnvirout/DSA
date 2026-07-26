class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp = []

        count = 0
        for num in nums:
            if num != 0:
                temp = temp + [num]
            else:
                count = count + 1
        
        nums[:] = temp
        nums.extend ([0] * count)

        return nums
        
        

