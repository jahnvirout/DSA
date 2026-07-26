class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high) // 2

            if nums[mid] == target:
                first = mid
                last = mid 

                while first > 0 and nums[first-1] == target:
                    first = first -1 
                while last < len(nums)-1 and nums[last+1] == target:
                    last = last + 1

                return [first,last]
            
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid -1


        return [-1,-1]