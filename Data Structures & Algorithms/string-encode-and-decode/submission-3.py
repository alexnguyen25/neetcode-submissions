class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans = ans + f"{len(i)}" + '#' + i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []


        index = 0
        count = 0
        while index < len(s):
            while s[index] != '#':
                index += 1

            length = int(s[count:index])
            ans.append(s[index + 1 : index + 1 + length])
            count = index + 1 + length
            index = count
        
        return ans