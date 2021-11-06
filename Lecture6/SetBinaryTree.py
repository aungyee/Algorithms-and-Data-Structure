# ---------------------------- Binary Search Tree Set ----------------------------- #

# To use a Binary Tree to implement a Set interface,
#   we use the traversal order of the tree to store the items sorted in increasing key order.
# This property is often called the Binary Search Tree Property,
#   where keys in a node’s left subtree are less than the key stored at the node,
#   and keys in the node’s right subtree are greater than the key stored at the node.
# Then finding the node containing a query key (or determining that no node contains the key)
#   can be done by walking down the tree, recursing on the appropriate side.

import BinaryNode
import BinaryTree


class BinarySearchTreeNode(BinaryNode):
    def subtree_find(self, k):                                                          # O(h)
        if k < self.item.key:
            if self.left:
                return self.left.subtree_find(k)
        elif k > self.item.key:
            if self.right:
                return self.right.subtree_find(k)
        else:
            return self
        return None

    def subtree_find_next(self, k):                                                     # O(h)
        if self.item.key <= k:
            if self.right:
                return self.right.subtree_find_next(k)
            else:
                return None
        elif self.left:
            A = self.left.subtree_find_next(k)
            if A:
                return A
        return self

    def subtree_find_prev(self, k):                                                     # O(h)
        if self.item.key >= k:
            if self.left:
                return self.left.subtree_find_prev(k)
            else:
                return None
        elif self.right:
            A = self.right.subtree_find_prev(k)
            if A:
                return A
        return self

    def subtree_insert(self, X):                                                        # O(h)
        if X.item.key < self.item.key:
            if self.left:
                self.left.subtree_insert(X)
            else:
                self.subtree_insert_before(X)
        elif X.item.key > self.item.key:
            if self.right:
                self.right.subtree_insert(X)
            else:
                self.subtree_insert_after(X)
        else:
            self.item = X.item


class SetBinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__(nodeType = BinarySearchTreeNode)

    def iter_order(self):
        yield from self

    def insert(self, x):
        newNode = self.nodeType(x)
        if self.root:
            self.root.subtree_insert(newNode)
            if newNode.parent is None:
                return False
        else:
            self.root = newNode
        self.size += 1
        return True

    def build(self, X):
        for x in X:
            self.insert(x)

    def find_min(self):
        if self.root:
            self.root.subtree_first().item

    def find_max(self):
        if self.root:
            self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node:
                return node.item

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:
                return node.item

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node:
                return node.item

    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None:
            self.root = None
        self.size -= 1
        return ext.item
