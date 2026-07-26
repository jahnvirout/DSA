class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pivot = len(nums) - 1

        # Find rotation point
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break

        # Decide which sorted half to search
        if nums[0] <= target <= nums[pivot]:
            low = 0
            high = pivot
        else:
            low = pivot + 1
            high = len(nums) - 1

        # Normal binary search
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1

                
        


