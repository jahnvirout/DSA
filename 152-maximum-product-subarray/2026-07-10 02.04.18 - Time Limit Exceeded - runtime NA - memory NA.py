class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        for i in range(len(nums)):
            product= 1

            for j in range(i, len(nums)):
               product = product * nums[j]
               max_product = max(product,max_product)
            
        return max_product