class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = words[::-1]
        result = " ".join(ans)
        return result


        


