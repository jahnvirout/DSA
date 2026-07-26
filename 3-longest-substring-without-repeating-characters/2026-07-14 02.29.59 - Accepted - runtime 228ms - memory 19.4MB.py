class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_strings = 0
        
        for i in range(len(s)):
            seen = set()
            count = 0

            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    count+=1
                else:
                    break
            
            max_strings = max(count,max_strings)
        return max_strings
        
