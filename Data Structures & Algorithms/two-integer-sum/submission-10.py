class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for idx, val in enumerate(nums):
            if target-val in d:
                return [d[target-val], idx]
            d[val] = idx
        
        return []
