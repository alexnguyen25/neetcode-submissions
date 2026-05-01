class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            cur = (l + r) // 2

            if nums[cur] < target:
                l = cur + 1
            elif nums[cur] > target:
                r = cur - 1
            elif nums[cur] == target:
                return cur
        return -1
        