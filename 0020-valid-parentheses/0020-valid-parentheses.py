class Solution:
    def isValid(self, s: str) -> bool:
        str_stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                str_stack.append(ch)
            else:
                if not str_stack:
                    return False
                elif ch == ')' and str_stack[-1] == '(':
                    str_stack.pop()
                elif ch == ']' and str_stack[-1] == '[':
                    str_stack.pop()
                elif ch == '}' and str_stack[-1] == '{':
                    str_stack.pop()
                else:
                    return False
        return len(str_stack) == 0