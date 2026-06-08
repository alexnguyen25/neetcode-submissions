class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = self.left(nums)
        right = self.right(nums)
        for i in range(len(nums)):
            if i <= 0:
                nums[i] = right[i + 1]
            elif i >= len(nums) - 1:
                nums[i] = left[i - 1]
            else:
                nums[i] = left[i - 1] * right[i + 1]
        return nums
        
    def left(self, nums):
        ans = []
        total = 1
        for i in nums:
            total *= i
            ans.append(total)
        return ans
    
    def right(self, nums):
        ans = []
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            ans.append(total)
        ans.reverse()
        return ans
