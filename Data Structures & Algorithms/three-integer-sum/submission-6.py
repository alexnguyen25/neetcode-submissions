class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        copy = sorted(nums)
        ans = []
        for i in range(len(copy) - 2):
            if i > 0 and copy[i - 1] == copy[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -copy[i]
            while l < r:
                check = copy[l] + copy[r]
                if check > target:
                    r -= 1
                elif check < target:
                    l += 1
                if check == target:
                    ans.append([copy[i], copy[l], copy[r]])
                    l += 1
                    r -= 1
                    while l < r and copy[l] == copy[l - 1]:
                        l += 1
                    while l < r and copy[r] == copy[r + 1]:
                        r -= 1

                
        
        return ans