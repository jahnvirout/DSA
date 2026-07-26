class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # LEFT half is sorted
            if nums[low] <= nums[mid]:

                # Target lies inside left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Target lies in right half
                else:
                    low = mid + 1

            # RIGHT half is sorted
            else:

                # Target lies inside right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # Target lies in left half
                else:
                    high = mid - 1

        return -1



