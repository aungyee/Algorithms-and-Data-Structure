# ------------------------------- Height Balanced Binary Tree ------------------------------ #
# Previously, we discussed binary trees as a general data structure for storing items,
#   without bounding the maximum height of the tree.
# The ultimate goal will be to keep our tree balanced: a tree on n nodes is balanced if its height is O(log n).
# Then all the O(h)-time operations we talked about last time will only take O(log n) time.

# There are many ways to keep a binary tree balanced under
#   insertions and deletions (Red-Black Trees, B-Trees, 2-3 Trees, Splay Trees, etc.).
# The oldest (and perhaps simplest) method is called an AVL Tree.
# Every node of an AVL Tree is height-balanced (i.e., satisfies the AVL Property)
#   where the left and right subtrees of a height-balanced node differ in height by at most 1.
# To put it a different way, define the skew of a node
#   to be the height of its right subtree minus the height of its left subtree
#   (where the height of an empty subtree is -1.)
# Then a node is height-balanced if it’s skew is either -1, 0, or 1.
# A tree is height-balanced if every node in the tree is height-balanced.
# Height-balance is good because it implies balance!


# ------------ Subtree Augmentation -------------- #
# Rebalancing requires us to check at least Ω(log n) heights in the worst-case,
#   so if we want rebalancing the tree to take at most O(log n) time,
#   we need to be able to evaluate the height of a node in O(1) time.
# Instead of computing the height of a node every time we need it, we will speed up computation via augmentation:
#   in particular each node stores and maintains the value of its own subtree height.
# Then when we’re at a node, evaluating its height is a simple as reading its stored value in O(1) time.
# However, when the structure of the tree changes,
#   we will need to update and recompute the height at nodes whose height has changed.

def height(A):                                                                  # O(1) for height augmentation
    if A:
        return A.height
    else:
        return -1


class BinaryNode:                                                               # O(1)
    def __init__(self, x):
        self.item = x
        self.parent = None
        self.left = None
        self.right = None
        self.subtree_update()

    def subtree_update(self):                                                   # O(1) for height augmentation
        self.height = 1 + max(height(self.left)) + max(height(self.right))

    # ------------- Rotation ---------------- #
    # As we add or remove nodes to our tree, it is possible that our tree will become imbalanced.
    # We will want to change the structure of the tree without changing its traversal order,
    #   in the hopes that we can make the tree’s structure more balanced.
    # We can change the structure of a tree using a local operation called a rotation.
    # A rotation takes a subtree that locally looks like one the following two configurations
    #   and modifies the connections between nodes in O(1) time to transform it into the other configuration.

    #                _____<D>__                     rotate_right(<D>)                   __<B>_____
    #            __<B>__      <E>                          =>                          <A>     __<D>__
    #          <A>     <C>    / \                                                      / \    <C>    <E>
    #          / \     / \   /___\                         <=                         /___\   / \    / \
    #         /___\   /___\                         rotate_left(<B>)                         /___\  /___\

    # This operation preserves the traversal order of the tree
    #   while changing the depth of the nodes in subtrees <A> and <E>.
    # Next time, we will use rotations to enforce that a balanced tree stays balanced
    #   after inserting or deleting a node.

    def subtree_rotate_right(D):                                               # O(1)
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A:
            A.parent = B
        if E:
            E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):                                                 # O(1)
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A:
            A.parent = B
        if E:
            E.parent = D
        B.subtree_update()
        D.subtree_update()

    # ------------- Maintaining Height-Balance ----------------- #
    # Suppose we have a height-balanced AVL tree, and we perform a single insertion or deletion
    #   by adding or removing a leaf.
    # Either the resulting tree is also height-balanced, or the change in leaf has made at least one node
    #   in the tree have magnitude of skew greater than 1.
    # In particular, the only nodes in the tree whose subtrees have changed after the leaf modification
    #   are ancestors of that leaf (at most O(h) of them), so these are the only nodes whose skew could have changed
    #   and they could have changed by at most 1 to have magnitude at most 2.
    # As shown in lecture via a brief case analysis, given a subtree whose root has skew is 2
    #   and every other node in its subtree is height-balanced,
    #   we can restore balance to the subtree in at most two rotations.
    # Thus to rebalance the entire tree, it suffices to walk from the leaf to the root,
    #   rebalancing each node along the way, performing at most O(log n) rotations in total.
    # A detailed proof is outlined in the lecture notes and is not repeated here;
    #   but the proof may be reviewed in recitation if students would like to see the Recitation 7.3 full argument.
    # Below is code to implement the rebalancing algorithm presented in lecture.

    def skew(self):                                                             # O(1)
        return height(self.right) - height(self.left)

    def rebalance(self):                                                        # O(1)
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left()
        elif self.skew() == -2:
            if self.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):                                                         # O(log n)
        self.rebalance()
        self.subtree_update()
        if self.parent:
            self.parent.maintain()

    # --------------- ^^^^ End Of AVL ^^^^ --------------- #

    def subtree_iter(self):                                                     # O(n)
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):                                                    # O(log n)
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):                                                     # O(log n)
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    def successor(self):                                                        # O(log n)
        if self.right:
            return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self = self.parent
        return self.parent

    def predecessor(self):                                                      # O(log n)
        if self.left:
            return self.left.subtree_last()
        while self.parent and (self is self.parent.left):
            self = self.parent
        return self.parent

    def subtree_insert_before(self, B):                                         # O(log n)
        if self.left:
            self = self.left.subtree_last()
            self.right, B.parent = B, self
        else:
            self.left, B.parent = B, self
        self.maintain()

    def subtree_insert_after(self, B):                                          # O(log n)
        if self.right:
            self = self.right.subtree_first()
            self.left, B.parent = B, self
        else:
            self.right, B.parent = B, self

    def subtree_delete(self):                                                   # O(log n)
        if self.left or self.right:
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            self.parent.maintain()
        return self
