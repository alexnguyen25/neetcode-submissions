class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + '#' + i
        return ans
            

    def decode(self, s: str) -> List[str]:
        index = 0
        ans = []

        while index < len(s):
            first = index
            while s[index] != '#':
                index += 1
            length = int(s[first:index])
            ans.append(s[index + 1 : index + 1 + length])
            index += length + 1


        return ans
            

