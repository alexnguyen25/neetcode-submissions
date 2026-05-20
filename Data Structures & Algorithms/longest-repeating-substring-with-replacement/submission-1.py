class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        butt = defaultdict(int)
        butt[s[l]] += 1 
        maxlength = 1

        while r < len(s):
            butt[s[r]] += 1

            if (r-l + 1) - max(butt.values()) > k:
                butt[s[l]] -= 1
                l += 1

            maxlength = max(maxlength, r - l + 1)
            r += 1


        return maxlength
