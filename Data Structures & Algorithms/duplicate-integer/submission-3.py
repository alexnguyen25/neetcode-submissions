class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        if len(test) != len(nums):
            return True
        return False