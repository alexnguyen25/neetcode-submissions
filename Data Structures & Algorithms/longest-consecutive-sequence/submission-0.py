class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashmap = defaultdict(int)
        sort = sorted(nums)
        for i in sort:
            hashmap[i] += 1
        copy = []
        for i in hashmap:
            copy.append(i)
        
        maxcount = 1
        count = 1
        for i in range(1, len(copy)):
            if copy[i] == (copy[i-1] + 1):
                count += 1
            else:
                count = 1
            maxcount = max(maxcount, count)
        
        return maxcount