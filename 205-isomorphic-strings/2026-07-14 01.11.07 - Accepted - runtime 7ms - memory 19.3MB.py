class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}
        i = 0
        for i in range(len(s)):
            if s[i] in mapST:
                if mapST[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapTS:
                    return False
        
            mapST[s[i]] = t[i]
            mapTS[t[i]] = s[i]
        return True
            