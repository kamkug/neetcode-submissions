# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        if root:
            q.append(root)

        res = []

        while q:
            q_len = len(q)
            for idx in range(q_len):
                curr = q.popleft()

                if idx == q_len-1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            rightSide = None
            q_len = len(q)

            for _ in range(q_len):
                rightSide = q.popleft()
                if rightSide.left:
                    q.append(rightSide.left)
                if rightSide.right:
                    q.append(rightSide.right)
            
            if rightSide:
                res.append(rightSide.val)
        
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth, result):
            if not node:
                return None
            
            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth+1, result)
            dfs(node.left, depth+1, result)
            
        result = []
        dfs(root, 0, result)

        return result
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [(root, 0)]
        res = []
        depth = 0

        while stack:
            node, depth = stack.pop()

            if depth == len(res):
                res.append(node.val)
            
            if node.left:
                stack.append((node.left, depth+1))

            if node.right:
                stack.append((node.right, depth+1))
        
        return res

       