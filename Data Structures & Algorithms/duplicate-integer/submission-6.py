class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            print(i)
            for j in range(len(nums)):
                if i == j:
                    continue
                print(j)
                if nums[i] == nums[j]:
                    return True
        
        return False