class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return false
        
        freq_s1 = Counter(s1)
        window = Counter()   
        left = 0

        for right in range(len(s2)):
            window[s2[right]] +=1

            if right - left + 1 > len(s1):
                window[s2[left]] -=1
                left+=1

            if right - left + 1 == len(s1):
                if window == freq_s1:
                    return True
        return False
        

