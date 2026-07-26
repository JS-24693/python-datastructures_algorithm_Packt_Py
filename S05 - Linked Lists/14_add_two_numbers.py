"""
Add Two Numbers (Linked List)

Adds two numbers represented as reversed linked lists.
Each node contains a single digit. Returns the head of a new list
representing the sum, also in reversed order.
"""

class Node:
    """A node containing a digit and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def add_two_numbers(l1, l2):
    """
    Add two reversed linked-list numbers and return the result list head.
    """
    head = None
    current = None
    carry = 0

    p1, p2 = l1, l2

    while p1 is not None or p2 is not None:
        s = carry

        if p1 is not None:
            s += p1.data
            p1 = p1.next

        if p2 is not None:
            s += p2.data
            p2 = p2.next

        digit = s % 10
        carry = s // 10

        new_node = Node(digit)

        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = current.next

    if carry > 0:
        current.next = Node(carry)

    return head


def traverse(head):
    """Print digits in the linked list."""
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next


# ---- Test Instantiation ----
# Number 3578 → 8 → 7 → 5 → 3
A = Node(8); A.next = Node(7); A.next.next = Node(5); A.next.next.next = Node(3)

# Number 296 → 6 → 9 → 2
B = Node(6); B.next = Node(9); B.next.next = Node(2)

result = add_two_numbers(A, B)

print("Result digits (reversed):")
traverse(result)

# 4
# 7
# 8
# 3
