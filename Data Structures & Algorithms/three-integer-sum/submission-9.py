class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        copy = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and copy[i] == copy[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                check = copy[i] + copy[l] + copy[r]
                if check < 0:
                    l += 1
                elif check > 0:
                    r -= 1
                else:
                    ans.append([copy[i],copy[l],copy[r]])
                    l+=1
                    r-=1
                    while l < r and copy[l] == copy[l - 1]:
                        l += 1
                    while l < r and copy[r] == copy[r + 1]:
                        r -= 1


        return list(ans)