"""
Singly Linked List: Delete at End

This module implements deletion of the last node in a singly linked list.
To delete the last node, we traverse to the second-last node and set its
`next` pointer to None. If the list contains only one node, deletion sets
`head = None`. This operation runs in O(n) time due to traversal.
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


def delete_at_end():
    """
    Delete the last node of the linked list.

    Cases:
    - Empty list → nothing to delete.
    - Single node → head = None.
    - Otherwise → traverse to second-last node and set next = None.
    """
    global head

    if head is None:
        return

    if head.next is None:
        head = None
        return

    current = head
    while current.next.next is not None:
        current = current.next

    current.next = None


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

delete_at_end()
print("\nAfter one deletion:")
traverse()

delete_at_end()
print("\nAfter two deletions:")
traverse()

# Before deletion:
# A
# B
# C
# D
# E

# After one deletion:
# A
# B
# C
# D

# After two deletions:
# A
# B
# C
