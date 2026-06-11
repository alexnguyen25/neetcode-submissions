class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + '#' + i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        while index < len(s):
            temp = index
            while s[index] != '#':
                index += 1
            length = int(s[temp:index])
            ans.append(s[index + 1: index + 1 + length])
            index += 1 + length
        return ans