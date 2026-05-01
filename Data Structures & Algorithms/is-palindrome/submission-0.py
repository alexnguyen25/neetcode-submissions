class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        fix = ""

        for i in lower:
            if i.isalnum():
                fix = fix + i

        l = 0
        r = len(fix) - 1
        
        for i in fix:
            if fix[l] != fix[r]:
                return False
            l += 1
            r -= 1
        return True
