"""
Remove Nth Node from End of List (One-Pass Two-Pointer Method)

Uses a fast pointer to create an N+1 gap so that slow pointer lands
just before the node to delete.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_nth_from_end(head, n):
    """
    Remove the Nth node from the end of the list and return the new head.
    """
    fast = head
    slow = head

    # Move fast pointer N+1 steps
    for _ in range(n + 1):
        if fast is None:
            # Cannot move N+1 steps → delete head
            return head.next
        fast = fast.next

    # Move both pointers until fast reaches None
    while fast:
        fast = fast.next
        slow = slow.next

    # slow.next is the node to delete
    slow.next = slow.next.next
    return head


def traverse(head):
    """Print list values."""
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next


# ---- Test Instantiation ----
# List: 1 → 2 → 3 → 4 → 5, remove N=2 → remove 4
nodes = [Node(i) for i in [1, 2, 3, 4, 5]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

new_head = remove_nth_from_end(head, 2)

print("List after removal:")
traverse(new_head)

# 1
# 2
# 3
# 5
