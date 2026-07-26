"""
Singly Linked List: Insert in Middle

This module implements insertion at an arbitrary position in a singly linked
list. To insert at position `pos`, we traverse to `pos-1`, then wire the new
node between current and current.next. If the list is empty or the position
is beyond the list length, the new node is inserted at the end.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


# Global head pointer
head = None


def insert_at(data, pos):
    """
    Insert a new node at position `pos`.

    Rules:
    - If list empty → new node becomes head.
    - If pos == 0 → insert at top.
    - If pos beyond list length → insert at end.
    - Otherwise traverse to pos-1 and rewire pointers.
    """
    global head
    NN = Node(data)

    # Empty list → new node becomes head
    if head is None:
        head = NN
        return

    # Insert at top
    if pos == 0:
        NN.next = head
        head = NN
        return

    # Traverse to pos-1
    current = head
    i = 0
    while i < pos - 1 and current.next is not None:
        current = current.next
        i += 1

    # Insert after current
    NN.next = current.next
    current.next = NN


def traverse():
    """Print all nodes from head to end."""
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
# Build initial list: A B C D
insert_at("A", 0)
insert_at("B", 1)
insert_at("C", 2)
insert_at("D", 3)

# Insert Z at position 2 → A B Z C D
insert_at("Z", 2)

# Insert X at position 1 → A X B Z C D
insert_at("X", 1)

# Insert Y at position 100 → appended → A X B Z C D Y
insert_at("Y", 100)

traverse()
