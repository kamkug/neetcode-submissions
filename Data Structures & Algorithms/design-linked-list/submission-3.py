class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next

        while curr is not self.right and index > 0:
            curr = curr.next
            index -= 1
        
        if curr is not self.right:
            return curr.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        old_head = self.left.next
        new_head = Node(val, self.left, old_head)
        self.left.next = old_head.prev = new_head  

    def addAtTail(self, val: int) -> None:
        old_tail = self.right.prev
        new_tail = Node(val, old_tail, self.right)
        self.right.prev = old_tail.next = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        prev, curr = self.left, self.left.next

        while curr and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        if curr:
            prev.next = curr.prev = Node(val, prev, curr)
            

    def deleteAtIndex(self, index: int) -> None:
        prev, curr = self.left, self.left.next

        while curr is not self.right and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        if curr is not self.right:
            prev.next = curr.next
            curr.next.prev = prev
            print(prev.next.val, curr.next.prev.val)
            print(self.right.prev.val)

            curr.prev = curr.next = None # clean up relationships to allow gc collect memory
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)