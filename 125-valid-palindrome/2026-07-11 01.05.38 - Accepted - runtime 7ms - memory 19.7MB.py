class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        rev = clean[::-1]

        if rev != clean:
            return False

        return True