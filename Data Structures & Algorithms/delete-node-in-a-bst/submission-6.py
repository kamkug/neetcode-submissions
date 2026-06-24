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
        
        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            return root
        
        replacement = None
        if not curr.left:
            replacement = curr.right
        elif not curr.right:
            replacement = curr.left
        else:
            successor_parent = curr
            successor = curr.right

            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            curr.val = successor.val

            if successor_parent is curr:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
            
            return root
        
        if not parent:
            return replacement
        
        if parent.left == curr:
            parent.left = replacement
        else:
            parent.right = replacement
        
        return root
