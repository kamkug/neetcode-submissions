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
        
        s = [(root, root.val)]

        while s:
            node, curr = s.pop()

            if not node.left and not node.right and curr == targetSum:
                return True
            
            if node.right:
                s.append((node.right, curr+node.right.val))
            
            if node.left:
                s.append((node.left, curr+node.left.val))
        
        return False
