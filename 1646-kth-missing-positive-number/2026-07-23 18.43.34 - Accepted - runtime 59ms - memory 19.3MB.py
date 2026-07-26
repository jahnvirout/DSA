class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        num = 1

        while True:
            if num not in arr:
                count+=1

                if count == k:
                    return num
            num+=1
            
    

