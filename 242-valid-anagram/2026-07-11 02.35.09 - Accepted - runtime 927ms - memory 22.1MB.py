class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        temp = []

        for ch in s:
            temp.append(ch.lower())

        for c in t:
            c = c.lower()

            if c in temp:
                temp.remove(c)
            else:
                return False

        return True
                

        

