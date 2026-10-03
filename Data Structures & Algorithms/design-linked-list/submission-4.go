type Node struct {
    val int
    prev, next *Node
}

func NewNode(val int, prev, next *Node) *Node {
    return &Node{val, prev, next}
}

type MyLinkedList struct {
    left, right *Node
}


func Constructor() *MyLinkedList {
    mll := MyLinkedList {
        left: NewNode(0, nil, nil),
        right: NewNode(0, nil, nil),
    }
    mll.left.next = mll.right
    mll.right.prev = mll.left
    return &mll
}


func (m *MyLinkedList) Get(index int) int {
    curr := m.left.next

    for curr != m.right && index > 0 {
        curr = curr.next
        index--
    }

    if curr != m.right {
        return curr.val
    }

    return -1
}


func (m *MyLinkedList) AddAtHead(val int)  {
    oldHead := m.left.next
    newHead := NewNode(val, m.left, oldHead)
    m.left.next = newHead
    oldHead.prev = newHead
}


func (m *MyLinkedList) AddAtTail(val int)  {
    oldTail := m.right.prev
    newTail := NewNode(val, oldTail, m.right)
    oldTail.next = newTail
    m.right.prev = newTail
}


func (m *MyLinkedList) AddAtIndex(index int, val int)  {
    prev, curr := m.left, m.left.next

    for curr != nil && index > 0 {
        prev = curr
        curr = curr.next
        index--
    }

    if curr != nil {
        node := NewNode(val, prev, curr)
        prev.next = node
        curr.prev = node
    }
}


func (m *MyLinkedList) DeleteAtIndex(index int)  {
    prev, curr := m.left, m.left.next

    for curr != m.right && index > 0 {
        prev = curr
        curr = curr.next
        index--
    }

    if curr != m.right {
        prev.next = curr.next
        curr.next.prev = prev
        curr.prev = nil
        curr.next = nil
    }
}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */