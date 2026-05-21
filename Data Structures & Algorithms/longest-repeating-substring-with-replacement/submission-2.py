class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength = 1
        l = 0
        r = 1
        hashmap = defaultdict(int)
        hashmap[s[l]] += 1

        while r < len(s):
            hashmap[s[r]] += 1
            if (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            r += 1
            maxlength = max(maxlength, r - l)
        return maxlength