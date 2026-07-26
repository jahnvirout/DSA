class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = nums[0]
        max_product = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_product, max_product = max_product, min_product

            max_product = max(nums[i], nums[i] * max_product)
            min_product = min(nums[i], nums[i] * min_product)

            ans = max(ans, max_product)

        return ans
