class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for i in nums:
            total += i
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preright = self.prefix[right]
        if left > 0:
            preleft = self.prefix[left - 1]
        else:
            preleft = 0

        return preright - preleft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)