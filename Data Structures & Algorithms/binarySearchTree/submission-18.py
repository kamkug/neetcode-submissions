class TreeNode:

    def __init__(self, key: int, val: int, left=None, right=None) -> None:
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return TreeNode(key, val)
            
            if node.key > key:
                node.left = dfs(node.left)
            elif node.key < key:
                node.right = dfs(node.right)
            else:
                node.val = val
            
            return node
        
        self.root = dfs(self.root)

    def get(self, key: int) -> int:
        if self.root is None:
            return -1

        curr = self.root

        while curr:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val

        return -1

    def getMin(self) -> int:
        if self.root is None:
            return -1
        
        curr = self.root

        while curr.left:
            curr = curr.left
        
        return curr.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        
        curr = self.root

        while curr.right:
            curr = curr.right
        
        return curr.val

    def remove_helper(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        
        return node

    def remove(self, key: int) -> None:
        def dfs(node: TreeNode, key) -> TreeNode:
            if node is None:
                return
            
            if node.key > key:
                node.left = dfs(node.left, key)
            elif node.key < key:
                node.right = dfs(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    min_node = self.remove_helper(node.right)
                    node.key = min_node.key
                    node.val = min_node.val
                    node.right = dfs(node.right, min_node.key)
            
            return node
        
        self.root = dfs(self.root, key)

    def getInorderKeys(self) -> List[int]:
        if self.root is None:
            return []

        curr = self.root
        stack = []
        res = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.key)
            curr = curr.right
        
        return res


        # curr = self.root
        # res = []

        # while curr:
        #     if curr.left is None:
        #         res.append(curr.key)
        #         curr = curr.right
        #     else:
        #         pred = curr.left
        #         while pred.right and pred.right is not curr:
        #             pred = pred.right
                
        #         if pred.right is None:
        #             pred.right = curr
        #             curr = curr.left
        #         else:
        #             pred.right = None
        #             res.append(curr.key)
        #             curr = curr.right
        
        # return res
