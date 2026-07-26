class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            # Target found
            if nums[mid] == target:
                return True

            # Cannot determine the sorted half because of duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1

            # Left half is sorted
            elif nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False