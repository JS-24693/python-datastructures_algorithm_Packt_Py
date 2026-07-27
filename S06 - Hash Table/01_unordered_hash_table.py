"""
hash_table.py

A simple hash table implementation using Python's built-in hash()
and modulo to map keys to array indices. It uses separate chaining 
(lists in each bucket) to handle collisions.

Python’s built‑in dict is significantly more optimized; 
this implementation is for instructional purposes only.
"""

class HashTable:
    """
    Minimal educational **unordered** hash table using separate chaining.

    - Hash the key.
    - Compute index = hash(key) % size.
    - Store (key, value) pairs in buckets (lists).
    - Collisions are handled by multiple entries in the same bucket.
    """
    def __init__(self, size=7):
        """
        Initialize the hash table with a fixed-size array.

        :param size: Number of buckets (array length).
        """
        self.size = size
        # Each bucket will hold a list of (key, value) pairs.
        self.table = [[] for _ in range(size)]  # main bucket array

    def _index(self, key):
        """
        Compute the array index for a given key:

            index = hash(key) % self.size

        Example:
        hash ("Toyota") = 79 → 79 % 7 = 2
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Insert or update a key–value pair.

        - Compute index from key.
        - Scan bucket for existing key.
        - Update or append (key, value) pair.
        """
        idx = self._index(key)
        bucket = self.table[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key, default=None):
        """
        Retrieve the value for a key.

        - 1. Compute the hash of the key.
        - 2. Compute the index using hash % size of the array.
        - 3. Scan the bucket at that index for the key.
        - 4. Return its value if found, otherwise return `default`.
        """
        idx = self._index(key)
        bucket = self.table[idx]

        for k, v in bucket:
            if k == key:
                return v

        return default

    def __repr__(self):
        """
        String representation showing the table and its bucket contents.
        """
        return f"HashTable(size={self.size}, table={self.table})"

    def __str__(self):
        """
        Human-readable string showing each index and its bucket contents.
        """
        lines = []
        for i, bucket in enumerate(self.table):
            lines.append(f"{i}: {bucket}")
        return "\n".join(lines)

if __name__ == "__main__":
    # Test instantiation and basic operations.

    # Create a hash table with 7 buckets.
    ht = HashTable(size=7)

    # Insert key–value pairs (human-selected values).
    ht.put("Toyota", 7)     
    ht.put("VW", 3)
    ht.put("Honda", 2.2)
    ht.put("Tesla", 1)

    # Retrieve values.
    print("Toyota:", ht.get("Toyota"))   # Toyota: 7
    print("VW:", ht.get("VW"))           # VW: 3
    print("Honda:", ht.get("Honda"))     # Honda: 2.2
    print("Tesla:", ht.get("Tesla"))     # Tesla: 1

    # Missing key example.
    print("BMW:", ht.get("BMW", default="not found"))  # BMW: not found

    # Show internal structure using __str__ (index → bucket).
    print("\nTable structure:")
    print(ht)
    # Example of output, but unordered hash table result may differ:
    # 0: []
    # 1: []
    # 2: [('Toyota', 7), ('Honda', 2.2)]
    # 3: []
    # 4: [('VW', 3)]
    # 5: []
    # 6: [('Tesla', 1)]

