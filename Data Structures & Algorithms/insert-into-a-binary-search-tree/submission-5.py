# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node
        
        curr = root

        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            elif val > curr.val:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
        
        return root

