class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ans = []
        count = 0
        for i in nums:
            if target - i in hashMap:
                if count < hashMap[target - i]:
                    ans.append(count)
                    ans.append(hashMap[target - i])
                else:
                    ans.append(hashMap[target - i])
                    ans.append(count)
            else:
                hashMap[i] = count
            count += 1
        return ans
            

        