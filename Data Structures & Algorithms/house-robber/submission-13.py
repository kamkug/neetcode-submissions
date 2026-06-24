class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = max(nums[-2:]), nums[-1]

        for i in range(len(nums)-3, -1, -1):
            prev1, prev2 = max(nums[i]+prev2, prev1), prev1
        
        return prev1