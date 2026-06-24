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

    def remove(self, key: int) -> None:
        if not self.tree:
            return
        
        parent = None
        curr = self.tree

        while curr and curr.key != key:
            parent = curr

            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                break
        
        if not curr:
            return
        
        replacement = None
        if not curr.left:
            replacement = curr.right
        elif not curr.right:
            replacement = curr.left
        else:
            successor_parent = curr
            successor = curr.right

            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            curr.key = successor.key
            curr.val = successor.val

            if successor_parent == curr:
                successor_parent.right = successor.left
            else:
                successor_parent.left = successor.left
            return
        
        if not parent:
            self.tree = replacement
        elif parent.left == curr:
            parent.left = replacement
        else:
            parent.right = replacement
        
    def getInorderKeys(self) -> List[int]:
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



        
        

