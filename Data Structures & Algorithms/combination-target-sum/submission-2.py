class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def inner(i, total, path):
            if total == target:
                result.append(path.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return

                path.append(nums[j])
                inner(j, total+nums[j], path)
                path.pop()
        
        inner(0, 0, [])
        return result


