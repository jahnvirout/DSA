class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
       freq_p = Counter(p)
       m = len(s)
       n = len(p)
       ans = []

       for i in range(m - n + 1):
        window = s[i: i+n]

        if Counter(window)  == freq_p:
            ans.append(i)

       return ans
    

    
