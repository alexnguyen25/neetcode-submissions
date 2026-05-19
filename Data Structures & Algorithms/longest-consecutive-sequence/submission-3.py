class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashmap = defaultdict(int)
        
        for i in nums:
            hashmap[i] += 1
        
        starters = []
        for i in hashmap:
            if i - 1 not in hashmap:
                starters.append(i)

        count = 1
        maxcount = 1
        for i in starters:
            temp = i
            go = True
            while go == True:
                if temp + 1 in hashmap:
                    count+=1
                    temp += 1
                else:
                    count = 1
                    go = False
                maxcount=max(maxcount, count)
        return maxcount