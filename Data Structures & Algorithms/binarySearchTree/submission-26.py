class TreeNode:

    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.tree = None

    def insert(self, key: int, val: int) -> None:
        def dfs(node, key, val):
            if not node:
                return TreeNode(key, val)
            
            if key < node.key:
                node.left = dfs(node.left, key, val)
            elif key > node.key:
                node.right = dfs(node.right, key, val)
            else:
                node.key = key
                node.val = val

            return node

        self.tree = dfs(self.tree, key, val)

    def get(self, key: int) -> int:
        def dfs(node):
            if not node:
                return -1
            
            if key < node.key:
                return dfs(node.left)
            elif key > node.key:
                return dfs(node.right)
            else:
                return node.val
            
        return dfs(self.tree)


    def getMin(self) -> int:
        if not self.tree:
            return -1

        curr = self.tree
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.tree:
            return -1

        curr = self.tree
        while curr.right:
            curr = curr.right
        return curr.val
    
    def get_min_node(self, node) -> TreeNode:
        if not node:
            return None
        
        curr = node
        while curr.left:
            curr = curr.left

        return curr

    def remove(self, key: int) -> None:
        def dfs(node, key):
            if not node:
                return
            
            if key < node.key:
                node.left = dfs(node.left, key)
            elif key > node.key:
                node.right = dfs(node.right, key)
            else:
                if not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                else:
                    min_node = self.get_min_node(node.right)
                    node.key = min_node.key
                    node.val = min_node.val
                    node.right = dfs(node.right, min_node.key)
            
            return node
        
        self.tree = dfs(self.tree, key)


    def getInorderKeys(self) -> List[int]:
        result = []

        print(self.tree)

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.key)
            dfs(node.right)
        dfs(self.tree)

        return result
        
        

