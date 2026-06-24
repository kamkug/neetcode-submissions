class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for right in range(0, len(nums)):
            if nums[right] in s:
                return True
            s.add(nums[right])

        return False
