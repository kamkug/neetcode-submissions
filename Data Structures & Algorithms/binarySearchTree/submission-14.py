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
            if not node:
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
        def dfs(node: TreeNode) -> int:
            nonlocal key

            if node is None:
                return -1
            
            if node.key > key:
                return dfs(node.left)
            elif node.key < key:
                return dfs(node.right)
            else:
                return node.val
            
        return dfs(self.root)

    def getMin(self) -> int:
        if self.root is None:
            return -1

        def dfs(node: TreeNode) -> int:
            if node.left is None:
                return node.val
            
            return dfs(node.left)
        
        return dfs(self.root)

    def getMax(self) -> int:
        if self.root is None:
            return -1

        def dfs(node: TreeNode) -> int:
            if node.right is None:
                return node.val
            
            return dfs(node.right)
        
        return dfs(self.root)
    
    def remove_helper(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        
        return node

    def remove(self, key: int) -> None:
        def dfs(node: TreeNode, key: int) -> TreeNode:
            if node is None:
                return None
            
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
        res = []

        def inorder(node: TreeNode) -> None:
            if node is None:
                return

            inorder(node.left)
            res.append(node.key)
            inorder(node.right)
        
        inorder(self.root)
        
        return res
