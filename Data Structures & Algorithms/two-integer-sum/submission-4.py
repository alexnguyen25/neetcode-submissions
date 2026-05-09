class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {nums[0] : 0}
        for i in range(1, len(nums)):
            check = target - nums[i]
            if check in hmap:
                return [hmap[check], i]
            else:
                hmap[nums[i]] = i
        return [0,0] 


        