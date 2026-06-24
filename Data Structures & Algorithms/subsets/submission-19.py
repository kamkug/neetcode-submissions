class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            result += [subset+[n] for subset in result]
        
        return result