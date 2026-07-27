def contains_duplicate(nums):
    """
    Return True if any integer appears at least twice in the list.

    Uses a hash table (dict) to track seen numbers.
    Time: O(N)
    Space: O(N)
    """
    seen = {}

    for n in nums:
        if n in seen:
            return True  # duplicate found
        seen[n] = True  # mark as seen

    return False  # no duplicates found

def contains_duplicate_set(nums):
    """
    Return True if any integer appears at least twice in the list.

    Uses a set for constant-time membership checks.
    Time: O(N)
    Space: O(N)
    """
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False

# Test Instantiation
if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [10, 20, 30]
    nums3 = [4, 5, 6, 4]

    print("\nDictionary version:")
    print("nums1:", contains_duplicate(nums1)) # nums1: True
    print("nums2:", contains_duplicate(nums2)) # nums2: False
    print("nums3:", contains_duplicate(nums3)) # nums3: True

    print("\nSet version:")
    print("nums1:", contains_duplicate_set(nums1)) # nums1: True
    print("nums2:", contains_duplicate_set(nums2)) # nums2: False
    print("nums3:", contains_duplicate_set(nums3)) # nums3: True
