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
        if not self.tree:
            self.tree = TreeNode(key, val)
        
        curr = self.tree
        while curr:
            if key < curr.key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            else:
                curr.key = key
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.tree
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1


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
        # morris traversal
        curr = self.tree
        result = []

        while curr:
            if not curr.left:
                result.append(curr.key)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    result.append(curr.key)
                    curr = curr.right
        
        return result



        
        

