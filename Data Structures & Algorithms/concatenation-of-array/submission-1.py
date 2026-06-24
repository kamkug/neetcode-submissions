class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))

        for idx in range(len(ans)):
            ans[idx] = nums[idx % len(nums)]
        
        return ans