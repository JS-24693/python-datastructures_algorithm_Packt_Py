class AlgorithmConceptualUnderstanding:
    @staticmethod
    def merge_sorted_arrays(A, B):
        """
        Merge two sorted lists A and B into a new sorted list C.
        Uses three pointers:
            i -> current index in A
            j -> current index in B
            k -> next insertion index in C
        Each iteration copies exactly one element from A or B.
        Time complexity: O(n + m), where n = len(A), m = len(B).
        """
        n = len(A)
        m = len(B)

        C = []  # result list
        i = j = 0

        # merge while both arrays have remaining elements
        while i < n and j < m:
            if A[i] <= B[j]:
                C.append(A[i])
                print(f"Placing {A[i]} into C at index {len(C)-1}: {C}")
                i += 1
            else:
                C.append(B[j])
                print(f"Placing {B[j]} into C at index {len(C)-1}: {C}")
                j += 1

        # copy remaining elements from A
        while i < n:
            C.append(A[i])
            print(f"Placing {A[i]} into C at index {len(C)-1}: {C}")
            i += 1

        # copy remaining elements from B
        while j < m:
            C.append(B[j])
            print(f"Placing {B[j]} into C at index {len(C)-1}: {C}")
            j += 1

        return C


if __name__ == "__main__":
    A = [5, 7, 9, 13, 20, 25, 32]
    B = [8, 11, 11, 15]
    C = AlgorithmConceptualUnderstanding.merge_sorted_arrays(A, B)
    print("Merged array:", C)

# Output of merging while both arrays have elements
# Placing 5 into C at index 0: [5]
# Placing 7 into C at index 1: [5, 7]
# Placing 8 into C at index 2: [5, 7, 8]
# Placing 9 into C at index 3: [5, 7, 8, 9]
# Placing 11 into C at index 4: [5, 7, 8, 9, 11]
# Placing 11 into C at index 5: [5, 7, 8, 9, 11, 11]
# Placing 13 into C at index 6: [5, 7, 8, 9, 11, 11, 13]
# Placing 15 into C at index 7: [5, 7, 8, 9, 11, 11, 13, 15]
# Placing 20 into C at index 8: [5, 7, 8, 9, 11, 11, 13, 15, 20]
# Placing 25 into C at index 9: [5, 7, 8, 9, 11, 11, 13, 15, 20, 25]
# Placing 32 into C at index 10: [5, 7, 8, 9, 11, 11, 13, 15, 20, 25, 32]
# Merged array: [5, 7, 8, 9, 11, 11, 13, 15, 20, 25, 32]

