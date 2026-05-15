class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(list)

        first = defaultdict(int)
        for i in nums:
            first[i] += 1
        
        for i, j in first.items():
            hashmap[j].append(i)
        
        ans = []
        for i in range(len(nums), 0, -1):
            if i in hashmap:
                ans.extend(hashmap[i])
            if len(ans) >= k:
                return ans
        
    
        return ans