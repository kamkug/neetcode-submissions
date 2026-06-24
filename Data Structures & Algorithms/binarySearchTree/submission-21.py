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
            elif node.key == key:
                node.val = val
            
            return node
            
        self.root = dfs(self.root)

    def get(self, key: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            
            if node.key > key:
                dfs(node.left)
            elif node.key < key:
                dfs(node.right)
            else:
                return node.val
            
            return -1

        return dfs(self.root)

    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root

        while curr and curr.left:
            curr = curr.left
        
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root

        while curr and curr.right:
            curr = curr.right
        
        return curr.val
    
    def remove_helper(self, node: TreeNode):
        if not node:
            return -1
        
        curr = node

        while node and node.left:
            node = node.left
        
        return node

    def remove(self, key: int) -> None:
        if not self.root:
            return
        
        def dfs(node: TreeNode, key: int) -> TreeNode:
            curr = node

            if curr.key > key:
                curr.left = dfs(node.left)
            elif curr.key < key:
                curr.right = dfs(node.right)
            else:
                if not curr.left:
                    return curr.right
                elif not curr.right:
                    return curr.left
                else:
                    min_node = self.remove_helper(node.right)
                    curr.key = min_node.key
                    curr.val = min_node.val
                    curr.right = dfs(node.right, min_node.key)
            
            return node
            
        self.root = dfs(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []

        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.key)
            dfs(node.right)

        dfs(self.root)
        return res
