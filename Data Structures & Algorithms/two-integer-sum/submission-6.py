class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in indices and indices[complement] != idx:
                return [idx, indices[complement]]
        
        return []