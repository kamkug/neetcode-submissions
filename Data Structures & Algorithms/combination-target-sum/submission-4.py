class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, path):
            if curr == target:
                result.append(path.copy())
                return

            if i == len(nums) or curr > target:
                return
            
            path.append(nums[i])
            dfs(i, curr + nums[i], path)
            path.pop()
            dfs(i+1, curr, path)
        
        dfs(0, 0, [])

        return result