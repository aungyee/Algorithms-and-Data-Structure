# ----------------------------- Binary Tree ------------------------------ #

# A binary tree is a tree (a connected graph with no cycles) of binary nodes:
#   a linked node container, similar to a linked list node, having a constant number of fields:
#       • a pointer to an item stored at the node,
#       • a pointer to a parent node (possibly None),
#       • a pointer to a left child node (possibly None), and
#       • a pointer to a right child node (possibly None).

# ---- Why is a binary node called “binary”? ---- #
# In actuality, a binary node can be connected to three other nodes
#   its parent, left child, and right child, not just two.
# However, we will differentiate a node’s parent from it’s children,
# and so we call the node “binary” based on the number of children the node has.


class BinaryNode:
    def __init__(self, x):                                                          # O(1)
        self.item = x
        self.left = None
        self.right = None
        self.parent = None
        # self.subtree_update()                 # Lecture 07

    # ---- Traversal Order ---- #

    # The nodes in a binary tree have a natural order based on the fact that
    #   we distinguish one child to be left and one child to be right.
    # We define a binary tree’s traversal order based on the following implicit characterization:
    #   • every node in the left subtree of node <X> comes before <X> in the traversal order; and
    #   • every node in the right subtree of node <X> comes after <X> in the traversal order.
    # Given a binary node <A>, we can list the nodes in <A>’s subtree by
    #   recursively listing the nodes in <A>’s left subtree, listing <A> itself,
    #   and then recursively listing the nodes in <A>’s right subtree.
    # This algorithm runs in O(n) time because every node is recursed on once doing constant work.

    def subtree_iter(self):                                                         # O(n)
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    # ---- Tree Navigation ---- #

    # Given a binary tree, it will be useful to be able to navigate the nodes in their traversal order efficiently.
    # Probably the most straight forward operation is to find the node in a given node’s subtree
    #   that appears first (or last) in traversal order.
    # To find the first node, simply walk left if a left child exists.
    # This operation takes O(h) time because each step of the recursion moves down the tree.
    # Find the last node in a subtree is symmetric.

    def subtree_first(self):                                                        # O(h)
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):                                                         # O(h)
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    # Given a node in a binary tree, it would also be useful too find the next node in the traversal order,
    #   i.e., the node’s successor, or the previous node in the traversal order, i.e., the node’s predecessor.
    # To find the successor of a node <A>, if <A> has a right child,
    #   then <A>’s successor will be the first node in the right child’s subtree.
    # Otherwise, <A>’s successor cannot exist in <A>’s subtree,
    #   so we walk up the tree to find the lowest ancestor of <A> such that <A> is in the ancestor’s left subtree.
    # In the first case, the algorithm only walks down the tree to find the successor, so it runs in O(h) time.
    # Alternatively in the second case, the algorithm only walks up the tree to find the successor,
    #   so it also runs in O(h) time. The predecessor algorithm is symmetric.

    def successor(self):                                                            # O(h)
        if self.right:
            return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self = self.parent
        return self.parent

    def predecessor(self):                                                         # O(h)
        if self.left:
            return self.left.subtree_last()
        while self.parent and (self is self.parent.left):
            self = self.parent
        return self.parent

    # ---- Dynamic Operation ---- #

    # If we want to add or remove items in a binary tree,
    #   we must take care to preserve the traversal order of the other items in the tree.
    # To insert a node <B> before a given node <A> in the traversal order, either node <A> has a left child or not.
    # If <A> does not have a left child, than we can simply add <B> as the left child of <A>.
    # Otherwise, if <A> has a left child, we can add <B>
    #   as the right child of the last node in <A>’s left subtree (which cannot have a right child).
    # In either case, the algorithm walks down the tree at each step, so the algorithm runs in O(h) time.
    # Inserting after is symmetric.

    def subtree_insert_before(self, B):                                            # O(h)
        if self.left:
            self = self.left.subtree_last()
            self.right, B.parent = B, self
        else:
            self.left, B.parent = B, self
        # self.maintain()                      # Lecture 07

    def subtree_insert_after(self, B):                                             # O(h)
        if self.right:
            self = self.right.subtree_first()
            self.left, B.parent = B, self
        else:
            self.right, B.parent = B, self
        # self.maintain()                      # Lecture 07

    # To delete the item contained in a given node from its binary tree, there are two cases
    #   based on whether the node storing the item is a leaf.
    # If the node is a leaf, then we can simply clear the child pointer from the node’s parent and return the node.
    # Alternatively, if the node is not a leaf, we can swap the node’s item
    #   with the item in the node’s successor or predecessor down the tree
    #   until the item is in a leaf which can be removed.
    # Since swapping only occurs down the tree, again this operation runs in O(h) time.

    def subtree_delete(self):                                                      # O(h)
        if self.left or self.right:            # if A is not a leaf
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:                        # if A is a leaf
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            # self.maintain()                  # Lecture 07
        return self
