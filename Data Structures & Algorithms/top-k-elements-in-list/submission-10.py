class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        inverted = defaultdict(list)

        for i in nums:
            count[i] += 1
        
        for i, j in count.items():
            inverted[j].append(i)
        
        ans = []
        for i in range(len(nums), 0, -1):
            if i in inverted:
                ans.extend(inverted[i])
            if len(ans) >= k:
                return ans

        return ans
        
        
        