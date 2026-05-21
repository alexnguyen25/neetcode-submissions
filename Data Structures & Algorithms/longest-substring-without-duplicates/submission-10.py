class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        hashmap = set()
        l = 0
        maxlength = 1
        r = 1
        hashmap.add(s[l])


        while r < len(s):
            if s[r] in hashmap:
                while s[r] in hashmap:
                    hashmap.remove(s[l])
                    l += 1
            else:
                hashmap.add(s[r])
                r += 1
            maxlength = max(maxlength, r - l)

        return maxlength