class Node:
    """
    Minimal BST node storing (key, value) pairs.
    """
    __slots__ = ("key", "value", "left", "right")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class OrderedMap:
    """
    Minimal educational **ordered** map using a balanced-like BST.

    - Keys are stored in sorted order.
    - Insert and lookup follow BST rules.
    - Worst-case and average-case complexity: O(log N) for balanced trees.
    - This implementation is instructional; it does not self-balance.

    This ordered map is a tree-based structure producing sorted order.
    It is different from Python’s OrderedDict, which preserves insertion order
    but does not sort keys.

    """

    def __init__(self):
        """
        Initialize an empty ordered map (BST root).
        """
        self.root = None

    def _insert(self, node, key, value):
        """
        Insert or update a key–value pair in BST order.
        """
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # update existing key

        return node

    def put(self, key, value):
        """
        Insert or update a key–value pair.

        - Traverse BST by comparing keys.
        - Insert new node or update existing node.
        """
        self.root = self._insert(self.root, key, value)

    def _search(self, node, key):
        """
        Search for a key in BST order.
        """
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def get(self, key, default=None):
        """
        Retrieve the value for a key.

        - Traverse BST using key comparisons.
        - Return value if found; else return default.
        """
        result = self._search(self.root, key)
        return result if result is not None else default

    def _inorder(self, node, out):
        """
        In-order traversal to list keys in sorted order.
        """
        if node is None:
            return
        self._inorder(node.left, out)
        out.append((node.key, node.value))
        self._inorder(node.right, out)

    def items(self):
        """
        Return all (key, value) pairs in sorted order.
        """
        out = []
        self._inorder(self.root, out)
        return out

    def __str__(self):
        """
        Human-readable sorted listing of (key, value) pairs.
        """
        pairs = self.items()
        return "\n".join(f"{k}: {v}" for k, v in pairs)

if __name__ == "__main__":
    om = OrderedMap()

    om.put("Toyota", 7)
    om.put("VW", 3)
    om.put("Honda", 2.2)
    om.put("Tesla", 1)

    print("Toyota:", om.get("Toyota"))                # Toyota: 7
    print("VW:", om.get("VW"))                        # VW: 3
    print("Honda:", om.get("Honda"))                  # Honda: 2.2
    print("Tesla:", om.get("Tesla"))                  # Tesla: 1
    print("BMW:", om.get("BMW", default="not found")) # BMW: not found

    print("\nSorted table:") # shows sorted order, not insertion order
    print(om)
    # Sorted table:
    # Honda: 2.2
    # Tesla: 1
    # Toyota: 7
    # VW: 3
    
    print("\nSorted items:", om.items()) # shows same sorted order in a Python list of tuples
    # Sorted items: [('Honda', 2.2), ('Tesla', 1), ('Toyota', 7), ('VW', 3)]

