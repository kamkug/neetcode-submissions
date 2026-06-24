class Solution:
    def rob(self, nums: List[int]) -> int:
        vals = [max(nums[-2:]), nums[-1]]

        for i in range(len(nums)-3, -1, -1):
            print(vals)
            tmp = vals[0]
            vals[0] = max(vals[0], nums[i]+vals[1])
            vals[1] = tmp

        return vals[0]