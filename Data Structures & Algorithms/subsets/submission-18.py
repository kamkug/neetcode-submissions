class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, path):
            if i == len(nums):
                result.append(path.copy())
                return None
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        return result