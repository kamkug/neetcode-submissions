class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(i, total, path):
            if total == target:
                result.append(path.copy())
            
            for j in range(i, len(nums)):
                if total+nums[j] > target:
                    return
                
                path.append(nums[j])
                dfs(j, total+nums[j], path)
                path.pop()
        
        dfs(0, 0, [])
        return result