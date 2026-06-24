/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        return nil
    }

    var parent *TreeNode
    curr := root

    for curr != nil && curr.Val != key {
        parent = curr

        if key < curr.Val {
            curr = curr.Left
        } else {
            curr = curr.Right
        }
    }

    if curr == nil {
        return root
    }

    var replacement *TreeNode
    if curr.Left == nil {
        replacement = curr.Right
    } else if curr.Right == nil {
        replacement = curr.Left
    } else {
        successorParent := curr
        successor := curr.Right

        for successor.Left != nil {
            successorParent = successor
            successor = successor.Left
        }

        curr.Val = successor.Val

        if successorParent == curr {
            successorParent.Right = successor.Right
        } else {
            successorParent.Left = successor.Right
        }

        return root
    }

    if parent == nil {
        return replacement
    } else if parent.Left == curr {
        parent.Left = replacement
    } else {
        parent.Right = replacement
    }

    return root
}

