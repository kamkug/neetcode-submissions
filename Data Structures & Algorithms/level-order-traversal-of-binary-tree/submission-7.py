# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        s = [(root, 0)]
        result = []

        while s:
            node, depth = s.pop()

            if len(result) == depth:
                result.append([node.val])
            else:
                result[depth].append(node.val)

            if node.right:
                s.append((node.right, depth+1))
            
            if node.left:
                s.append((node.left, depth+1))

        return result
                
            
                