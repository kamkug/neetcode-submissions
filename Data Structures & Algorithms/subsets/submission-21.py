class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, path):
            result.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()
        
        dfs(0, [])
        
        return result
