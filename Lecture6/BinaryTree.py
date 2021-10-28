# ----------------------------- Binary Tree ------------------------------ #

# All of the operations we have defined so far have been within the Binary Tree class,
#   so that they apply to any subtree.
# Now we can finally define a general Binary Tree data structure
#   that stores a pointer to its root, and the number of items it stores.
# We can implement the same operations with a little extra work to keep track of the root and size.

import BinaryNode


class BinaryTree:
    def __init__(self, nodeType = BinaryNode):                                  # O(1)
        self.root = None
        self.size = 0
        self.nodeType = nodeType

    def __len__(self):                                                          # O(1)
        return self.size

    def __iter__(self):                                                         # O(n)
        if self.root:
            for A in self.root.subtree_iter():
                yield A.item
