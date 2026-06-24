# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def dfs(node):
            nonlocal res, k
            if not node:
                return res
            
            if dfs(node.left) > 0:
                return res
            k -= 1
            if k == 0:
                res = node.val
                return res

            if dfs(node.right) > 0:
                return res
            
            return res
            
        return dfs(root)

