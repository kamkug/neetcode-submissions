class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()
            dfs(i+1, subset, total)

        dfs(0, [], 0)

        return res
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                
                subset.append(nums[j])
                dfs(j, subset, total + nums[j])
                subset.pop()
        
        dfs(0, [], 0)
        return res
