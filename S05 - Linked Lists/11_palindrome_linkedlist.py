"""
Palindrome Linked List (O(n) time, O(1) space)

This module checks whether a singly linked list is a palindrome by:
1. Finding the midpoint.
2. Reversing the second half iteratively.
3. Comparing both halves.
"""

class Node:
    """A node containing data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class PalindromeChecker:
    """Encapsulates helper methods for palindrome detection."""

    def find_length(self, head):
        """Return the length of the list."""
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    def find_node_at(self, head, pos):
        """Return the node at index `pos` (0-based)."""
        current = head
        count = 0
        while count < pos and current:
            current = current.next
            count += 1
        return current

    def reverse_half(self, start, previous):
        """
        Reverse the list starting at `start` until None.
        Reconnect using `previous`.
        """
        A = start
        B = start.next

        while A and B:
            temp = B.next
            B.next = A
            A = B
            B = temp

        # Fix pointers after reversal
        start.next = None
        previous.next = A

    def is_palindrome(self, head):
        """Return True if list is palindrome, False otherwise."""
        if head is None or head.next is None:
            return True

        n = self.find_length(head)

        # Determine reverse start index
        if n % 2 == 0:
            reverse_pos = n // 2
        else:
            reverse_pos = n // 2 + 1

        # Locate nodes
        start = self.find_node_at(head, reverse_pos)
        previous = self.find_node_at(head, reverse_pos - 1)

        # Reverse second half
        self.reverse_half(start, previous)

        # Compare halves
        first = head
        second = previous.next

        while first and second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next

        return True


def traverse(head):
    """Print list values."""
    current = head
    while current:
        print(current.data)
        current = current.next


# ---- Test Instantiation ----
# Build palindrome list: 1 → 2 → 3 → 2 → 1
nodes = [Node(i) for i in [1, 2, 3, 2, 1]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

checker = PalindromeChecker()
print("Is Palindrome:", checker.is_palindrome(head)) # Is Palindrome: True
