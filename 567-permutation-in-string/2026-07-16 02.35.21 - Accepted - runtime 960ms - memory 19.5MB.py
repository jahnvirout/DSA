class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        freq_s1 = Counter(s1)  #a:1 b:1

        if m>n:
            return False
        
        for i in range(n-m+1):
            window = s2[i:i+m]

            if Counter(window) == freq_s1:
                return True
        return False
