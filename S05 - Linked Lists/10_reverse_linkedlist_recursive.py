"""
Reverse a Singly Linked List (Recursive Approach)

This module implements a recursive linked-list reversal. The recursive
function reverses the list from the current node onward and rewires pointers
as the recursion unwinds. The last node becomes the new head.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListReverser:
    """Encapsulates recursive reversal logic and stores the new head."""
    def __init__(self):
        self.new_head = None

    def reverse(self, node):
        """
        Recursively reverse the list starting at `node`.
        Returns the last node of the reversed sublist.
        """
        # Base case: last node
        if node.next is None:
            self.new_head = node
            return node 

        # Recursive case
        last = self.reverse(node.next)
        last.next = node
        return node

    def reverse_list(self, head):
        """Public method to reverse the entire list and return new head."""
        if head is None:
            return None

        last = self.reverse(head)
        last.next = None  # original head becomes last node
        return self.new_head


def traverse(head):
    """Print all nodes from head to end."""
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
# Build list: 1 → 2 → 3 → 4 → 5 → 6
nodes = [Node(i) for i in [1, 2, 3, 4, 5, 6]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

print("Original List:")
traverse(head)

reverser = LinkedListReverser()
new_head = reverser.reverse_list(head)

print("\nReversed List:")
traverse(new_head)

# Original List:
# 1
# 2
# 3
# 4
# 5
# 6

# Reversed List:
# 6
# 5
# 4
# 3
# 2
# 1
