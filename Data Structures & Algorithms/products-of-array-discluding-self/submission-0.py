class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = []
        total = 1
        for i in nums:
            total *= i
            pref.append(total)
        
        post = []
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            post.insert(0, total)

        print(pref)
        print(post)
        ans = []
        for i in range(len(nums)):
            l = 0 
            r = 0
            if i > 0:
                l = pref[i - 1]
            else:
                l = 1
            if i < len(nums) - 1:
                r = post[i + 1]
            else:
                r = 1
            ans.append(l*r)
        return ans