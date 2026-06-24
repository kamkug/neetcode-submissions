# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, curr):
            if not node:
                return False
           
            return (
                (node.left is None and node.right is None and curr+node.val == targetSum) or
                dfs(node.left, curr+node.val) or
                dfs(node.right, curr+node.val)
            )
        
        return dfs(root, 0)
