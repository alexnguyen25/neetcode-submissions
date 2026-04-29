class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                nums[index + 1] = nums[i]
                index += 1
        return index + 1

            
        