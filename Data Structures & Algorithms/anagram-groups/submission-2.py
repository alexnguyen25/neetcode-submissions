class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            lets = [0] * 26
            for c in s:
                lets[ord(c) - ord('a')] += 1
            ans[tuple(lets)].append(s)
        
        return list(ans.values())