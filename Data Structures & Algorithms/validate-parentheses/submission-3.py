class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'[' : ']', '{' : '}', '(' : ')'}
        stack = []
        for i in s:
            if i in hmap:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if hmap[stack.pop()] != i:
                    return False

        return len(stack) == 0

        