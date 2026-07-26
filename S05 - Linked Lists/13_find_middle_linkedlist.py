"""
Find Middle of Linked List (Slow–Fast Pointer Method)

Returns the middle node of a singly linked list.
If the list has an even number of nodes, returns the second middle.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    """
    Return the middle node using slow–fast pointer technique.
    Slow moves 1 step, fast moves 2 steps.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def traverse(head):
    """Print list values."""
    current = head
    while current:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
# List: 1 → 2 → 3 → 4 → 5 → 6
nodes = [Node(i) for i in [1, 2, 3, 4, 5, 6]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

middle = find_middle(head)
print("Middle Node:", middle.data) # Middle Node: 4
