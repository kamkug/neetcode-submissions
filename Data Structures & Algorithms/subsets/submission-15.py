class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
    
        subset = []
        result = []

        def dfs(s, e):
            result.append(subset[:])  # [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]

            for i in range(s, e):
                subset.append(nums[i])
                dfs(i+1, e)
                subset.pop()

        dfs(0, len(nums))
        return result