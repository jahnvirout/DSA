class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)
        window = Counter()
        ans = []
        left = 0
        for right in range(len(s)):
            window[s[right]] +=1

            if right - left + 1 > len(p):
                window[s[left]]-=1
                
                if window[s[left]]==0:
                    del window[s[left]]

                left+=1

            if window == freq_p:
                ans.append(left)
        return ans

