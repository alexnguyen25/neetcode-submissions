class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(list)

        cat = defaultdict(int)
        for i in range(len(nums)):
            cat[nums[i]] += 1

        #nums[i] is the actual number
        #cat is nums[i] = #frequency

        for i, j in cat.items():   # i = number, j = frequency
            hashmap[j].append(i)
        
        ans = []       
        for i in range(len(nums), 0, -1):  # start from max possible frequency
            if i in hashmap:
                ans.extend(hashmap[i])
            if len(ans) >= k:
                return ans
        return ans