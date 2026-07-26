"""
Detect Cycle in a Linked List (Floyd's Tortoise and Hare)

This module implements the optimal O(n) / O(1)-space algorithm for detecting
a cycle in a singly linked list. Two pointers move at different speeds; if
they ever meet, a cycle exists.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    """
    Return True if the linked list contains a cycle, otherwise False.

    Rules:
    - Empty list or single node → no cycle.
    - Use slow (1 step) and fast (2 steps) pointers.
    - If fast reaches None → no cycle.
    - If slow == fast → cycle detected.
    """
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


# ---- Test Instantiation ----
# Build list: 3 → 2 → 0 → -4 → (cycle back to 2)

n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2   # cycle

print("Cycle detected:", has_cycle(n1)) # Cycle detected: True
