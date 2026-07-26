class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            next = intervals[i]

            if next[0]<=current[1]:
                current[1] = max(next[1],current[1])

            else:
                ans.append(current)
                current = next 
        
        ans.append(current)
        return ans