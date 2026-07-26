class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lastS = {}
        lastT= {}
        for i in range(len(s)):
            if lastS.get(s[i]) != lastT.get(t[i]):
                return False
            
            lastS[s[i]] = i
            lastT[t[i]] = i
        return True

        