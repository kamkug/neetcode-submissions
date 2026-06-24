class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        len_nums = 1 << len(nums)

        for i in range(len_nums):
            subset = [nums[j] for j in range(len_nums) if i& 1 << j != 0]
            result.append(subset)
        
        return result