class QuickSort:
    @staticmethod
    def partition(A):
        """
        Partition list A around its last element (pivot).
        All elements <= pivot are moved to the left side.
        Pivot is placed in its correct final position.
        Returns the pivot's final index.
        Time complexity: O(n)
        """
        n = len(A)
        pivot = A[n - 1]
        left = -1  # boundary of <= pivot region

        # scan all elements except pivot
        for i in range(n - 1):
            if A[i] <= pivot:
                left += 1
                A[left], A[i] = A[i], A[left]

        # place pivot after all <= pivot elements
        left += 1
        A[left], A[n - 1] = A[n - 1], A[left]

        return left

# Test instantiation
if __name__ == "__main__":
    A = [2, 5, 1, 0, 4, 6, 3]
    print("Before partition:", A)
    pivot_index = QuickSort.partition(A)
    print("After partition :", A)
    print("Pivot final index:", pivot_index)

# Before partition: [2, 5, 1, 0, 4, 6, 3]
# After partition : [2, 1, 0, 3, 4, 6, 5]
# Pivot final index: 3