class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + '#' + i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            temp = i
            while s[i] != '#':
                i += 1
            length = int(s[temp:i])

            ans.append(s[i + 1 : i + 1 + length])
            i += 1 + length
        return ans