# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        inorder_indexes = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def helper(start, end) -> Optional[TreeNode]:
            nonlocal preorder_idx
    
            if start >= end:
                return None
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            index = inorder_indexes[root.val]

            root.left = helper(start, index)
            root.right = helper(index+1, end)

            return root
        
        return helper(0, len(preorder))


