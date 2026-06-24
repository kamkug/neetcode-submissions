# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        curr = root
        result = []

        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if pred.right == curr:
                    pred.right = None
                    result.append(curr.val)
                    curr = curr.right
                else:
                    pred.right = curr
                    curr = curr.left
        
        return result

