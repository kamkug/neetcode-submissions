# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        curr = root
        if key < curr.val:
            curr.left = self.deleteNode(curr.left, key)
        elif key > curr.val:
            curr.right = self.deleteNode(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                min_val = self.get_min(curr.right)
                curr.val = min_val
                curr.right = self.deleteNode(curr.right, min_val)
        
        return curr
    
    def get_min(self, node: Optional[TreeNode]) -> int:
        curr = node
        while curr.left:
            curr = curr.left
        return curr.val