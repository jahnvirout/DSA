class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            ans = ""
            i = 0

            while i<len(word) and i< len(prefix):
                if word[i] == prefix[i]:
                    ans = ans + word[i]
                    i+=1
                
                else:
                    break

            prefix = ans
            
            
        return ans

