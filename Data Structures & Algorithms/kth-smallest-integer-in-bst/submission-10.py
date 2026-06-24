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
            nonlocal k

            if not node:
                return 0
            
            if res := dfs(node.left):
                return res
            
            k -= 1
            if k == 0:
                return node.val
            
            if res := dfs(node.right):
                return res
        
        return dfs(root)
            
