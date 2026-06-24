class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.left = Node((0, 0))
        self.right = Node((0, 0), self.left)
        self.left.next = self.right
    
    def _remove_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.prev = node.next = None

    def _insert_node(self, node):
        old_tail, right_dummy = self.right.prev, self.right
        old_tail.next = right_dummy.prev = node
        node.next = right_dummy
        node.prev = old_tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._insert_node(node)
            return node.val[1]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
        
        self.cache[key] = Node((key, value))
        self._insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove_node(lru)
            del self.cache[lru.val[0]]
        
