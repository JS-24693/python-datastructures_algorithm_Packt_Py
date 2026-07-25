class AlgorithmConceptualUnderstanding:
    @staticmethod
    def selection_sort(li):
        """
        Perform an in-place selection sort on list `li`.
        For each index i, find the smallest element in li[i:]
        and swap it with li[i]. Time complexity: O(n^2).
        """
        n = len(li)

        for i in range(n):  # outer loop: position where smallest should be placed
            small_index = i  # assume smallest is at i

            # scan unsorted region to find actual smallest
            for j in range(i, n):
                if li[j] < li[small_index]:
                    small_index = j

            # swap smallest found with element at position i
            print(f"Putting {li[small_index]} at index {i}")
            li[i], li[small_index] = li[small_index], li[i]

# Test Selection Sorting
if __name__ == '__main__':
    data = [10, 25, 20, 50, 45, 15, 40]
    AlgorithmConceptualUnderstanding.selection_sort(data)
    print("Sorted data:", data) 

# Putting 10 at index 0
# Putting 15 at index 1
# Putting 20 at index 2
# Putting 25 at index 3
# Putting 40 at index 4
# Putting 45 at index 5
# Putting 50 at index 6
# Sorted data: [10, 15, 20, 25, 40, 45, 50]