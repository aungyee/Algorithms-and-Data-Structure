# --------------------------- Sequence Binary Tree ------------------------------ #

# ------------- Size Augmentation -------------- #
# To use a Binary Tree to implement a Sequence interface,
#   we use the traversal order of the tree to store the items in Sequence order.
# Now we need a fast way to find the ith item in the sequence because traversal would take O(n) time.
# If we knew how many items were stored in our left subtree,
#   we could compare that size to the index we are looking for and recurse on the appropriate side.
# In order to evaluate subtree size efficiently, we augment each node in the tree with the size of its subtree.
# A node’s size can be computed in constant time given the sizes of its children by summing them and adding 1.

from HeightBalancedBinaryTree import BinaryNode
from Lecture6.BinaryTree import BinaryTree


class SizeNode(BinaryNode):
    def subtree_update(self):                                               # O(1)
        super().subtree_update()
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def subtree_at(self, i):                                               # O(h)
        assert i >= 0
        if self.left:
            L_size = self.left.size
        else:
            L_size = 0
        if i < L_size:
            return self.left.subtree_at(i)
        elif i > L_size:
            return self.right.subtree_at(i - L_size - 1)
        else:
            return self

# --------------- Sequence AVL -------------- #
# Once we are able to find the ith node in a balanced binary tree in O(log n) time,
# the remainder of the Sequence interface operations can be implemented directly using binary tree operations.
# Further, via the first exercise in R06, we can build such a tree from an input sequence in O(n) time.
# We call this data structure a Sequence AVL.


class SequenceBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__(SizeNode)

    def build(self, X):
        def build_subtree(X, i, j):
            c = (i + j) // 2
            root = self.nodeType(X[c])
            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root
            if i > c:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root
        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size

    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item

    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        newNode = self.nodeType(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(newNode)
            else:
                self.root = newNode
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(newNode)
        self.size += 1

    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete
        if ext.parent is None:
            self.root = None
        self.size -= 1
        return ext.item

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)
