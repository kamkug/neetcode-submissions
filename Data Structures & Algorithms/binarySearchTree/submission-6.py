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
        
        def insert_helper(node: TreeNode):
            nonlocal key, val
            if node is None:
                return TreeNode(key, val)
            
            if node.key > key:
                node.left = insert_helper(node.left)
            elif node.key < key:
                node.right = insert_helper(node.right)
            else:
                node.val = val

            return node

        insert_helper(self.root)

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        
        curr = self.root

        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
            else:
                break
        else:
            return -1
        
        return curr.val

    def getMin(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root

        while curr.left:
            curr = curr.left
        
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        
        while curr.right:
            curr = curr.right
        
        return curr.val
    
    def remove_helper(self, node: TreeNode) -> int:
        if not node:
            return -1

        curr = node

        while curr.left:
            curr = curr.left
        
        return curr

    def remove(self, key: int) -> None:
        if not self.root:
            return
    
        def dfs_remove(node: TreeNode, key: int) -> TreeNode:
            if not node:
                return None

            if node.key < key:
                node.right = dfs_remove(node.right, key)
            elif node.key > key:
                node.left = dfs_remove(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else: 
                    curr = self.remove_helper(node.right)
                    node.key = curr.key
                    node.val = curr.val
                    node.right = dfs_remove(node.right, curr.key)
            
            return node
        
        self.root = dfs_remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []

        curr = self.root

        while curr:
            if curr.left is None:
                res.append(curr.key)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.key)
                    curr = curr.right

        return res
