"""
Singly Linked List: Insert at Top (Front)

This module implements dynamic insertion at the front of a singly linked list.
A new node becomes the new head, and its `next` pointer references the previous
head. If the list is empty, the new node simply becomes the head.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


# Global head pointer for the list
head = None


def insert_at_top(data):
    """
    Insert a new node at the front of the linked list.

    Steps:
    1. Create new node NN.
    2. If list empty → head = NN.
    3. Otherwise → NN.next = head; head = NN.
    """
    global head
    NN = Node(data)

    if head is None:
        head = NN
    else:
        NN.next = head
        head = NN


def traverse():
    """Print all nodes from head to end."""
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
insert_at_top("A")
insert_at_top("B")
insert_at_top("E")
insert_at_top("C")

traverse()

# C
# E
# B
# A
