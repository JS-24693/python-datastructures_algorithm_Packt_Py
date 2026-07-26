"""
Singly Linked List: Insert at End

This module implements dynamic insertion at the end of a singly linked list.
To insert, we traverse until the last node (where next == None) and attach the
new node. If the list is empty, the new node becomes the head.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


# Global head pointer
head = None


def insert_at_end(data):
    """
    Insert a new node at the end of the linked list.

    Steps:
    1. Create new node NN.
    2. If list empty → head = NN.
    3. Otherwise traverse until last node.
    4. Set last_node.next = NN.
    """
    global head
    NN = Node(data)

    if head is None:
        head = NN
        return

    current = head
    while current.next is not None:
        current = current.next

    current.next = NN


def traverse():
    """Print all nodes from head to end."""
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
insert_at_end("A")
insert_at_end("B")
insert_at_end("C")
insert_at_end("D")

# Insert at top to verify both methods work together
def insert_at_top(data):
    global head
    NN = Node(data)
    NN.next = head
    head = NN

insert_at_top("Z")

traverse()

# Z
# A
# B
# C
# D