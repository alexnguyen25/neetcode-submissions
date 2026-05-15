class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]

        for i in range(len(nums)):
            colors[nums[i]] += 1
        
        index = 0
        for i in range(len(colors)):
            for j in range(colors[i]):
                nums[index] = i
                index += 1
        
        