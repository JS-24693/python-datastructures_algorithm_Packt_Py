"""
dict_hash_table.py

A minimal educational demonstration showing how Python's built‑in `dict`
functions as a highly optimized hash table.

Python's `dict` provides:
- O(1) average insert, lookup, delete
- automatic resizing
- insertion‑order preservation (Python 3.7+)
- efficient memory layout and collision handling

This file contrasts with manual hash‑table implementations by showing
how simple the interface becomes when using Python's built‑in structure.
"""


class DictHashTable:
    """
    Thin wrapper around Python's built‑in dict to emphasize its role
    as a hash table with O(1) average operations.
    """

    def __init__(self):
        self._map = {}

    def put(self, key, value):
        """Insert or update a key–value pair."""
        self._map[key] = value

    def get(self, key, default=None):
        """Retrieve value for key or return default."""
        return self._map.get(key, default)

    def delete(self, key):
        """Remove key; raise KeyError if missing."""
        del self._map[key]

    def __str__(self):
        """Human‑readable listing in insertion order."""
        return ", ".join(f"{k}: {v}" for k, v in self._map.items())


if __name__ == "__main__":
    # Simple demonstration
    d = DictHashTable()
    d.put("Toyota", 4.5)
    d.put("VW", 3)
    d.put("Honda", 2.2)
    d.put("Tesla", 1)
    d.put("Toyota", 7)  # update

    print("Dict‑based hash table:")
    print(d)
    # Dict‑based hash table:
    # Toyota: 8, VW: 3, Honda: 2.2, Tesla: 1

    print("\nLookups:")
    print("Toyota:", d.get("Toyota"))
    print("BMW:", d.get("BMW", default="not found"))

    # Lookups:
    # Toyota: 7
    # BMW: not found