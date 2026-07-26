class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        low = 0
        high = len(nums) - 1

        # Find pivot
        pivot = len(nums) - 1

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break

        # Decide which half to search
        if nums[0] <= target <= nums[pivot]:
            low = 0
            high = pivot
        else:
            low = pivot + 1
            high = len(nums) - 1

        # Normal Binary Search
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False
