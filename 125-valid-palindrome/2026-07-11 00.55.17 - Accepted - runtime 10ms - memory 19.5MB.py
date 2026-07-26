class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left].isalnum() != True:
                left += 1

            elif s[right].isalnum() != True:
                right -= 1

            elif s[right].lower() != s[left].lower():
                return False

            else:
                left += 1
                right -= 1

        return True
        
