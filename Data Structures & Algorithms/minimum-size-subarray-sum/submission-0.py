class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0

        ans = 9999999

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                total -= nums[l]
                ans = min(ans, r - l + 1)
                l += 1

        
        return 0 if ans == 9999999 else ans
