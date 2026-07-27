class AVLNode:
    """
    Minimal AVL tree node storing (key, value) pairs.

    - height is maintained for rebalancing.
    """
    __slots__ = ("key", "value", "left", "right", "height")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # leaf height


class OrderedHashTable:
    """
    Strict educational self-balancing ordered map using an AVL tree.

    - Keys are stored in sorted order.
    - Insert and lookup are O(log N) (height-balanced tree).
    - This is a tree-based ordered structure, not Python's OrderedDict.
    """

    def __init__(self):
        """
        Initialize an empty ordered map (AVL root).
        """
        self.root = None

    # ---------- AVL helpers ----------

    def _height(self, node):
        return node.height if node is not None else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        """
        Rebalance node if its balance factor is out of [-1, 1].
        """
        self._update_height(node)
        bf = self._balance_factor(node)

        # Left heavy
        if bf > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right heavy
        if bf < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # ---------- core operations ----------

    def _insert(self, node, key, value):
        """
        Insert or update a key–value pair, then rebalance.
        """
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        return self._rebalance(node)

    def put(self, key, value):
        """
        Insert or update a key–value pair in AVL order.

        - Traverse by key comparisons.
        - Rebalance after insertion.
        """
        self.root = self._insert(self.root, key, value)

    def _search(self, node, key):
        """
        Search for a key in AVL tree.
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

        - Traverse AVL tree using key comparisons.
        - Return value if found; else return default.
        """
        result = self._search(self.root, key)
        return result if result is not None else default

    # ---------- traversal ----------

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
    # Test instantiation and basic operations.
    om = OrderedHashTable()

    om.put("Toyota", 7)
    om.put("VW", 3)
    om.put("Honda", 2.2)
    om.put("Tesla", 1)

    print("Toyota:", om.get("Toyota"))  # Toyota: 7
    print("VW:", om.get("VW"))  # VW: 3
    print("Honda:", om.get("Honda"))  # Honda: 2.2
    print("Tesla:", om.get("Tesla"))  # Tesla: 1
    print("BMW:", om.get("BMW", default="not found"))  # BMW: not found

    print("\nSorted table:")  # shows height-balanced sorted order, not insertion order
    print(om)
    # Sorted table:
    # Honda: 2.2
    # Tesla: 1
    # Toyota: 7
    # VW: 3

    print("\nSorted items:", om.items())  # shows same sorted order in a Python list of tuples
    # Sorted items: [('Honda', 2.2), ('Tesla', 1), ('Toyota', 7), ('VW', 3)]
