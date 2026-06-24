class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(s, curr, path):
            if curr == target:
                result.append(path.copy())
            
            for j in range(s, len(nums)):
                if curr + nums[j] > target:
                    return

                path.append(nums[j])
                dfs(j, curr + nums[j], path)
                path.pop()
        
        dfs(0, 0, [])

        return result