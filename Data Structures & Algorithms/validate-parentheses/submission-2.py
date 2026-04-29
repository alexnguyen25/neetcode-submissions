class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {'{' : '}', '[' : ']', '(' : ')'}

        for c in s:
            if c in close:
                stack.append(c)
            elif len(stack) == 0 or close[stack.pop()] != c:
                return False
        return len(stack) == 0
        