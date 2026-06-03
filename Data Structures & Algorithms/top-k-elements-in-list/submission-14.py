class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        rev = defaultdict(list)
        for i, j in freq.items():
            rev[j].append(i)
        
        ans = []
        for i in range(len(nums), 0, -1):
            if i in rev:
                ans.extend(rev[i])
            if len(ans) >= k:
                return ans
        return ans