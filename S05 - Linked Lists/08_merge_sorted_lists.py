"""
Merge Two Sorted Linked Lists

This module merges two sorted singly linked lists using the classic
two‑pointer technique. Nodes are reused (spliced), not recreated.
Time: O(m + n)
Space: O(1)
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_lists(head1, head2):
    """
    Merge two sorted linked lists and return the head of the merged list.
    Uses a tail pointer for O(1) append operations.
    """
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Dummy node to simplify tail handling
    dummy = Node(None)
    tail = dummy

    p1, p2 = head1, head2

    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    # Append remaining nodes
    tail.next = p1 if p1 is not None else p2

    return dummy.next


def traverse(head):
    """Print all nodes from head to end."""
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
# List1: 1 → 2 → 4
A1 = Node(1)
A2 = Node(2)
A3 = Node(4)
A1.next = A2
A2.next = A3

# List2: 1 → 3 → 4
B1 = Node(1)
B2 = Node(3)
B3 = Node(4)
B1.next = B2
B2.next = B3

merged = merge_sorted_lists(A1, B1)

print("Merged List:")
traverse(merged)

# Merged List:
# 1
# 1
# 2
# 3
# 4
# 4
