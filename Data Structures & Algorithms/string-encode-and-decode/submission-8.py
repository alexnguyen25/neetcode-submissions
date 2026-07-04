class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        r = 0
        ans = []
        while r < len(s):
            l = r
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            ans.append(s[r + 1 : r + 1 + length])
            r += 1 + length
        return ans
