class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =  []

        def backtrack(i, total, path):
            if total == target:
                result.append(path.copy())
                return
            
            if i == len(nums) or total > target:
                return
            
            path.append(nums[i])
            backtrack(i, total+nums[i], path)
            path.pop()
            backtrack(i+1, total, path)
        
        backtrack(0, 0, [])
        return result
    
    # target = 9, array = [2, 5, 6, 9]

    # 1 -> 0, 0, []
    # 2 -> 0, 2, [2]
    # 3 -> 0, 4, [2, 2]
    # 4 -> 0, 6, [2, 2, 2]

