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

        
    def remove(self, key: int) -> None:
        if not self.root:
            return None
        
        curr = self.root
        parent = None

        while curr and curr.key != key:
            parent = curr

            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            return None
        
        replacement = None
        if not curr.left:
            replacement = curr.right
        elif not curr.right:
            replacement = curr.left
        else:
            parent_successor = curr
            successor = curr.right
            while curr.left:
                parent_successor = curr
                curr = curr.left
            
            if parent_successor is curr:
                parent_successor.left = successor.right
            else:
                parent_successor.right = successor.right
            
            return
        
        if not parent:
            self.root = replacement
        elif parent == curr:
            self.left = replacement
        else:
            self.right = replacement

    def remove(self, key: int) -> None:
        if not self.root:
            return None
        
        curr = self.root
        parent = None

        while curr and curr.key != key:
            parent = curr

            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return None
        
        if not curr.left:
            replacement = curr.right
        elif not curr.right:
            replacement = curr.left
        else:
            pred_parent = curr
            pred = curr.left

            while pred.right:
                pred_parent = pred
                pred = pred.right
                            
            curr.key = pred.key
            curr.val = pred.val
            
            if pred_parent is curr:
                pred_parent.left = pred.left
            else:
                pred_parent.right = pred.left
            
            return

        
        if parent is None:
            self.root = replacement
        elif parent.left is curr:
            parent.left = replacement
        else:
            parent.right = replacement


    def remove(self, key: int) -> None:
        def dfs(node: TreeNode, key: int) -> TreeNode:
            if not self.root:
                return None
            
            if key < node.key:
                node.left = dfs(node.left)
            elif key > node.key:
                node.right = dfs(node.right)
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