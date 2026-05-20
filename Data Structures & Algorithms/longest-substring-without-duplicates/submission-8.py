class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlength = 1
        r = 1
        if not s:
            return 0
        
        ray = s[l]
        while r < len(s):
            if s[r] in ray:
                while s[r] in ray:
                    l += 1
                    ray = s[l:r]
            else:
                ray += s[r]
                r += 1
            maxlength = max(maxlength, len(ray))
        return maxlength
        