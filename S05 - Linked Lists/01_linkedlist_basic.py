"""
Basic Singly Linked List Manual Implementation

This module demonstrates how to manually create nodes, link them together,
and traverse a singly linked list. Each node stores `data` and a reference
to the next node. Traversal begins at `head` and continues until `None`.
"""

class Node:
    """A node in a singly linked list containing data and a next pointer."""
    def __init__(self, data):
        self.data = data      # store the value
        self.next = None      # reference to the next node (initially None)

# ---- Manual Linked List Construction ----

# Create nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

# Link nodes together
A.next = B
B.next = C
C.next = D

# Head points to the first node
head = A

# ---- Traversal and Printing ----
current = head
while current is not None:
    print(current.data)
    current = current.next

# A
# B
# C
# D

