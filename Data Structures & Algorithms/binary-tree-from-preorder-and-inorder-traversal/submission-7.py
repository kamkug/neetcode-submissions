# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = i = 0

        def dfs(limit: int) -> Optional[TreeNode]:
            nonlocal p, i

            if p >= len(preorder):
                return None
            
            if limit == inorder[i]:
                i += 1
                return None
            
            root = TreeNode(preorder[p])
            p += 1


            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root
        
        return dfs(1001)