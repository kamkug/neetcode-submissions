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
        if not self.root:
            self.root = TreeNode(key, val)
            return

        curr = self.root

        while curr:
            if curr.key > key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    break

                curr = curr.left
            elif curr.key < key:
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    break

                curr = curr.right
            elif curr.key == key:
                curr.val = val
                break

    def get(self, key: int) -> int:
        if not self.root:
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
        if not self.root:
            return -1

        def dfs(node: TreeNode) -> int:
            return node.val if not node.left else dfs(node.left)
        
        return dfs(self.root)

    def getMax(self) -> int:
        if not self.root:
            return -1

        def dfs(node: TreeNode) -> int:
           return node.val if not node.right else dfs(node.right)
        
        return dfs(self.root)
    
    def remove_helper(self, node: TreeNode):
        if not node:
            return -1
        
        curr = node

        while node and node.left:
            node = node.left
        
        return node

    # Fixed version
    def remove(self, key: int) -> None:
        if not self.root:
            return
        
        def dfs(node: TreeNode, key: int) -> TreeNode:
            if not node:
                return None
                
            if key < node.key:
                node.left = dfs(node.left, key)
            elif key > node.key:
                node.right = dfs(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = self.remove_helper(node.right)
                    node.key = min_node.key
                    node.val = min_node.val
                    node.right = dfs(node.right, min_node.key)
            
            return node
            
        self.root = dfs(self.root, key)

    def getInorderKeys(self) -> List[int]:
        if not self.root:
            return []

        curr = self.root
        res = []

        while curr:
            if not curr.left:
                res.append(curr.key)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.key)
                    curr = curr.right
        
        return res