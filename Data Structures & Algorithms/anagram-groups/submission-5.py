class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            lets = [0] * 26
            for c in i:
                lets[ord(c) - ord('a')] += 1
            ans[tuple(lets)].append(i)
        return list(ans.values())