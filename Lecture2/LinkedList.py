# ------------------ Sequence Interface ----------------- #
# Sequences maintain a collection of items in an extrinsic order
# Each item stored has a rank in the sequence, including a first item and a last item
# By extrinsic, we mean that the first item is ‘first’,
#   not because of what the item is, but because some external party put it there
# Sequences are generalizations of stacks and queues, which support a subset of sequence operations.

# -- Sequence Operation  -- #
# 1. Container #
#   build(x) - given an iterable X, build sequence from items in X
#   len() - return the number of stored items
# 2. Static #
#   iter_seq() - return the stored items one-by-one in sequence order
#   get_at(i) - return the ith item
#   set_at(i, x) - replace the ith item with x
# 3. Dynamic #
#   insert_at(i, x) - add x as the ith item
#   delete_at(i) - remove and return the ith item
#   insert_first(x) - add x as the first item
#   delete_first() - remove and return the first item
#   insert_last(x) - add x as the last item
#   delete_last() - remove and return the last item

# -- Implementation -- #
# Three implementation will be discussed
#   1. Array
#   2. Linked List or Pointer
#   3. Dynamic Array

# Linked List Sequence #

# A linked list is a different type of data structure entirely.
# Instead of allocating a contiguous chunk of memory in which to store items,
#   a linked list stores each item in a node, node, a constant-sized container with two properties:
#          1. node.item storing the item
#          2. node.next storing the memory address of the node containing the next item in the sequence

class LinkedListNode:
    def __init__(self, x):                                                  # O(1)
        self.item = x
        self.next = None

    def later_node(self, i):                                                # O(i)
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class LinkedListSeq:
    def __init__(self):                                                     # O(1)
        self.head = None
        self.size = 0

    def __len__(self):                                                      # O(1)
        return self.size

    def __iter__(self):                                                     # O(n)
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):                                                     # O(n)
        for x in reversed(X):
            self.insert_first(x)

    def get_at(self, i):                                                    # O(i)
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):                                                 # O(i)
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):                                              # O(1)
        newNode = LinkedListNode(x)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def delete_first(self):                                                 # O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):                                              # O(i)
        if i == 0:
            self.insert_first(x)
            return
        newNode = LinkedListNode(x)
        node = self.head.later_node(i - 1)
        newNode.next = node.next
        node.next = newNode
        self.size += 1

    def delete_at(self, i):                                                 # O(i)
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):                                               # O(n)
        self.insert_at(len(self), x)

    def delete_last(self):                                                  # O(n)
        self.delete_at(len(self) - 1)





