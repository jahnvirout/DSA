class Solution:
    def largestOddNumber(self, stringss: str) -> str:
        empty_str = ""

        for i in range(len(stringss)):
            if int(stringss[i]) % 2 != 0:
                empty_str = stringss[:i+1]

        return empty_str