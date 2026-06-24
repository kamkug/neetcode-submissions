class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for idx, num in enumerate(nums):
            complement = target-num
            
            if num in complements:
                return [complements[num], idx]
            
            complements[complement] = idx

        return []