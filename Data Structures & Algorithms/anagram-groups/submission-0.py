class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        if len(strs) == 1 or len(strs) == 0:
            return [strs]

        for string in strs:
            word = ''.join(sorted(string))
            if word in ans:
                ans[word].append(string)
            else:
                ans[word] = [string]
        conc = []
        for i in ans:
            conc.append(ans[i])
        return conc
            
        