class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

        inverted = defaultdict(list)
        for i, j in freq.items():
            inverted[j].append(i)
        
        print(inverted)
        
        count = len(nums)
        ans = []
        timer = k
        while k > 0:
            if count in inverted:
                for word in (inverted[count]):
                    ans.append(word)
                    k -= 1
                    if k == 0:
                        return ans
            count -= 1
        return ans
