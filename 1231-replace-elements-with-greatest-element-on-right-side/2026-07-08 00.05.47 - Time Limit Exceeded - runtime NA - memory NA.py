class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            current_max = -1
            for j in range(i+1, len(nums)):
                if nums[j] > current_max:
                    current_max= nums[j]
            answer.append(current_max)
                
        return answer

                


        