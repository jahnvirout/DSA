class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        max_right = -1
        for i in range (len(nums)-1,-1,-1):
            temp = nums[i]
            nums[i] = max_right
            max_right = max(temp,max_right)

        return nums

        

                


        