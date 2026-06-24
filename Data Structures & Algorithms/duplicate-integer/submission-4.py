class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            if nums.count(n) > 1:
                return True
        
        return False