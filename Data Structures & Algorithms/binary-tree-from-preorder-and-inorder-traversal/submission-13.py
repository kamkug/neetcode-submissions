# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = in_idx = 0

        def dfs(limit):
            nonlocal pre_idx, in_idx

            if pre_idx >= len(preorder):
                return
            
            if limit == inorder[in_idx]:
                in_idx += 1
                return
            
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root
        
        return dfs(1001)