class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {nums[0] : 0}
        for i in range(1, len(nums)):
            if target - nums[i] in hmap:
                return [hmap[target-nums[i]], i]
            else:
                hmap[nums[i]] = i
        return [0,0] 


        