class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        combinations = 1 << len(nums)

        for i in range(combinations):
            subset = [nums[j] for j in range(len(nums)) if i & 1 << j]
            result.append(subset)
        
        return result
    
   #  [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]