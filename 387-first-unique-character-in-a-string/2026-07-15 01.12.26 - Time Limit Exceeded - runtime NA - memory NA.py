class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            count = 0
            for j in range(len(s)):
                if s[i] == s[j]:
                    count +=1

            if count == 1:
                return i
        return -1

