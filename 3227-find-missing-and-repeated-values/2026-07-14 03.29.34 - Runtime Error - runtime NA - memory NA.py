class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        def repeatedval():
         for rows in grid:
             for num in rows:
                 if num == num1:
                     return num
        
        def repeatedvals():
            for rows in grid:
                for num in rows:
                    if num + 1 
