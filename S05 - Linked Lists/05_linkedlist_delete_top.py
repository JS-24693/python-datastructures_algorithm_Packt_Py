"""
Singly Linked List: Delete at Top

This module implements deletion of the first node in a singly linked list.
Deletion is performed by updating `head` to `head.next`. If the list is empty,
no deletion occurs. This operation runs in O(1) time.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


# Global head pointer
head = None


def insert_at_end(data):
    """Helper method to build a list for testing."""
    global head
    NN = Node(data)
    if head is None:
        head = NN
        return
    current = head
    while current.next is not None:
        current = current.next
    current.next = NN


def delete_at_top():
    """
    Delete the first node of the linked list.

    If head is None → nothing to delete.
    Otherwise → head = head.next.
    """
    global head
    if head is not None:
        head = head.next


def traverse():
    """Print all nodes from head to end."""
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
# Build list A B C D E
for x in ["A", "B", "C", "D", "E"]:
    insert_at_end(x)

print("Before deletion:")
traverse()

delete_at_top()
print("\nAfter one deletion:")
traverse()

delete_at_top()
print("\nAfter two deletions:")
traverse()

# Before deletion:
# A
# B
# C
# D
# E

# After one deletion:
# B
# C
# D
# E

# After two deletions:
# C
# D
# E
