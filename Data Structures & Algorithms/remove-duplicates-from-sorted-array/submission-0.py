class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[left-1]:
                nums[left] = nums[i]
                left += 1
        
        return left