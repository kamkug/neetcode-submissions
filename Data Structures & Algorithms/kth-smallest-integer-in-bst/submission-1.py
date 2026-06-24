# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return res[k-1]
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = 0

        def inorder(root):

            nonlocal counter
            if root is None:
                return
            
            nonlocal res

            inorder(root.left)

            counter += 1
            if counter == k:
                res = root.val
            
            inorder(root.right)

            return res

        return inorder(root)
    

        def kthSmallest(root: Optional[ListNode], k: int) -> int:
            stack = []
            curr = root

            while curr and stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                
                node = stack.pop()
                
                k -= 1
                if k == 1:
                    return node.val

                curr = curr.right

            return 0