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

        q = deque([(root, targetSum)])

        while q:
            node, curr_sum = q.popleft()

            if node.left is None and node.right is None and node.val-curr_sum == 0:
                return True
            
            if node.left:
                q.append((node.left, curr_sum-node.val))
            
            if node.right:
                q.append((node.right, curr_sum-node.val))
        
        return False
