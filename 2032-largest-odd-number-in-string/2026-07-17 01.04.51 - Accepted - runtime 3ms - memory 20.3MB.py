class Solution:
    def largestOddNumber(self, stringss: str) -> str:
        empty_str = ""

        for i in range(len(stringss)-1,-1,-1):
            if int(stringss[i]) % 2 == 1:
                empty_str = stringss[:i+1]
                break

        return empty_str