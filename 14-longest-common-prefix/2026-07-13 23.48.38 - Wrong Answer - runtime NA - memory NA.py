class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        i = 0
        ans = ""
        for word in strs[1:]:
            if word[i] == prefix[i]:
                ans += word[i]
                i+=1
        
        return ans



