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
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {k: v for v, k in enumerate(preorder)}
        preorder_index = 0
        
        def dfs(in_left, in_right):
            nonlocal preorder_index
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            index = mapping[root.val]
            root.left = dfs(in_left, index-1)
            root.right = dfs(index+1, in_left)

            return root
        
        return dfs(0, len(preorder)-1)
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = in_idx = 0

        def dfs(limit): 
            nonlocal pre_idx, in_idx, preorder

            if pre_idx >= len(preorder):
                return None
            
            if limit == inorder[in_idx]:
                in_idx += 1
                return None
            
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root
        
        return dfs(float(math.inf))
