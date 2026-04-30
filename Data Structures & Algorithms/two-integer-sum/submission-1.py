class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        count = 0
        for i in nums:
            if target - i in hmap:
                return [hmap[target - i], count]
            else:
                hmap[i] = count
            count += 1
        return [2,2]

        