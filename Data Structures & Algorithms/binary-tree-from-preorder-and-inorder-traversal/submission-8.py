# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = preorder_idx = 0

        def inner(limit):
            nonlocal preorder_idx, inorder_idx

            if preorder_idx >= len(preorder):
                return None
            
            if limit == inorder[inorder_idx]:
                inorder_idx += 1
                return None
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1

            root.left = inner(root.val)
            root.right = inner(limit)

            return root
        
        return inner(1001)