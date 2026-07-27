"""
OrderedDict implemented using a hash table + doubly linked list.

This structure preserves insertion order while providing:
- O(1) average insert, lookup, and delete
- Ordered iteration over keys
- Hash-table-based mapping (unlike BST-based ordered maps)

This is a minimal educational implementation similar in spirit to
Python's OrderedDict, but simplified for clarity.
"""


class _Node:
    """Doubly linked list node storing (key, value)."""
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class OrderedHashDict:
    """
    Minimal ordered dictionary using:
    - A hash table for O(1) average lookup
    - A doubly linked list to preserve insertion order
    """

    def __init__(self):
        self._map = {}          # key -> node
        self._head = None       # first node
        self._tail = None       # last node

    def __setitem__(self, key, value):
        """Insert or update a key–value pair."""
        if key in self._map:
            self._map[key].value = value
            return

        node = _Node(key, value)
        self._map[key] = node

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

    def __getitem__(self, key):
        """Retrieve value for key; raise KeyError if missing."""
        if key not in self._map:
            raise KeyError(key)
        return self._map[key].value

    def __delitem__(self, key):
        """Remove key from dictionary."""
        if key not in self._map:
            raise KeyError(key)

        node = self._map.pop(key)

        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev

    def items(self):
        """Yield (key, value) pairs in insertion order."""
        cur = self._head
        while cur:
            yield (cur.key, cur.value)
            cur = cur.next

    def __iter__(self):
        """Iterate over keys in insertion order."""
        cur = self._head
        while cur:
            yield cur.key
            cur = cur.next

    def __str__(self):
        """Human-readable listing."""
        return ", ".join(f"{k}: {v}" for k, v in self.items())


if __name__ == "__main__":
    # Simple test / demonstration
    d = OrderedHashDict()
    d["banana"] = 7
    d["apple"] = 3
    d["cherry"] = 2
    d["banana"] = 8  # update

    print("Ordered items:")
    print(d)
    # Ordered items:
    # banana: 8, apple: 3, cherry: 2

    print("\nIterating:")
    for k, v in d.items():
        print(k, v)
        # Iterating:
        # banana 8
        # apple 3
        # cherry 2