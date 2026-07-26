"""
Intersection of Two Linked Lists

This module finds the intersection node of two singly linked lists.
The algorithm:
1. Compute lengths of both lists.
2. Advance pointer in the longer list so both pointers have equal remaining length.
3. Move both pointers together until they meet.
4. If they meet, return the intersection node; otherwise return None.

Time: O(M + N)
Space: O(1)
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    """Return the length of a linked list."""
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


def get_intersection(headA, headB):
    """
    Return the intersection node of two linked lists, or None if no intersection.
    """
    if headA is None or headB is None:
        return None

    lenA = length(headA)
    lenB = length(headB)

    fp = headA
    sp = headB

    # Align pointers
    if lenA < lenB:
        for _ in range(lenB - lenA):
            sp = sp.next
    else:
        for _ in range(lenA - lenB):
            fp = fp.next

    # Walk together
    while fp is not None and sp is not None:
        if fp is sp:
            return fp
        fp = fp.next
        sp = sp.next

    return None


# ---- Test Instantiation ----
# Build intersection manually:
# A: A1 → A2 → C1 → C2
# B: B1 → B2 → B3 → C1 → C2

A1 = Node("A1")
A2 = Node("A2")
B1 = Node("B1")
B2 = Node("B2")
B3 = Node("B3")
C1 = Node("C1")
C2 = Node("C2")

# Link A list
A1.next = A2
A2.next = C1
C1.next = C2

# Link B list
B1.next = B2
B2.next = B3
B3.next = C1  # intersection

intersection = get_intersection(A1, B1)
print("Intersection Node:", intersection.data if intersection else None)
# Intersection Node: C1
