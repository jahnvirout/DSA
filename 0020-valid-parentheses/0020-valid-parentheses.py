class Solution:
    def isValid(self, s: str) -> bool:
        str_stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
            }

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
               str_stack.append(ch)
            else:
                if not str_stack or str_stack[-1] != pairs[ch]:
                    return False
                str_stack.pop ()
            
        return len(str_stack) == 0

        


            