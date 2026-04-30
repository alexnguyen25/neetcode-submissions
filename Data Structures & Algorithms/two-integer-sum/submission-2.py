class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        count = 0
        for i in nums:
            ans = target - i
            if ans in hmap:
                return [hmap[ans], count]
            else:
                hmap[i] = count
            count += 1
        return [2,2]

        