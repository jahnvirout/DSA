class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = []
        count = 0
        for ch in s:
            temp.append(ch.lower())

            for c in t:
                if c in temp:
                    temp.remove(c)
            
        if len(temp) != 0:
            return False
        else:
            return True


                

        

