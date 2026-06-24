class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = 1 << len(nums)

        for i in range(n):
            subset = [nums[j] for j in range(len(nums)) if i & 1 << j != 0]
            result.append(subset)
        
        return result