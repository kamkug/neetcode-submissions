# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def dfs(s, e):
            nonlocal preorder_idx
            if s > e:
                return
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            index = inorder_dict[root.val]

            root.left = dfs(s, index-1)
            root.right = dfs(index+1, e)

            return root

        return dfs(0, len(inorder)-1)