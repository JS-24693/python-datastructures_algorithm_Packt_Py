"""
Linked List Cycle II — Find Cycle Start (Floyd’s Algorithm)

This module detects whether a cycle exists in a singly linked list.
If a cycle exists, it returns the node where the cycle begins.
Time: O(n)
Space: O(1)
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle_start(head):
    """
    Return the node where the cycle begins, or None if no cycle exists.

    Phase 1: Detect cycle using slow/fast pointers.
    Phase 2: Move head pointer and meeting pointer together to find start.
    """
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    meeting_point = None

    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            meeting_point = slow
            break

    if meeting_point is None:
        return None  # no cycle

    # Phase 2: Find cycle start
    start = head
    while start != meeting_point:
        start = start.next
        meeting_point = meeting_point.next

    return start


# ---- Test Instantiation ----
# Build list: 3 → 2 → 0 → -4 → (cycle back to 2)

n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2   # cycle start at node with value 2

cycle_start = detect_cycle_start(n1)
print("Cycle starts at:", cycle_start.data if cycle_start else None) # Cycle starts at: 2
