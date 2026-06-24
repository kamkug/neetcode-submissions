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
                return False
            
            if dfs(node.left):
                return True
            k -= 1
            if k == 0:
                res = node.val
                return True

            if dfs(node.right):
                return True
            
        dfs(root)

        return res

