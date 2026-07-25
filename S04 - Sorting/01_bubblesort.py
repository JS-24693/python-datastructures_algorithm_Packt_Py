class AlgorithmConceptualUnderstanding:
    @staticmethod
    def bubble_sort(li):
        """
        Perform an in-place bubble sort on list `li`.
        Compares adjacent elements and swaps when out of order.
        Time complexity: O(n^2).
        """
        n = len(li)                     # length of list

        # Using range(n - 1) performs exactly the number of passes bubble sort needs.
        # Changing to range(n) adds one extra outer iteration.
        # That final iteration executes an empty inner loop (no comparisons, no swaps).
        # Sorting remains correct, but the algorithm performs one redundant pass.
        for i in range(n - 1):          # outer loop: n-1 passes

            for j in range(n - i - 1):  # inner loop: shrink unsorted region
                if li[j] > li[j + 1]:   # adjacent out of order
                    li[j], li[j + 1] = li[j + 1], li[j]  # swap

# Test Bubble Sorting:
if __name__ == '__main__':
    # Instantiate caller variable (list to be sorted)
    data = [64, 34, 12]

    # Call the bubble sort function (in-place modification)
    AlgorithmConceptualUnderstanding.bubble_sort(data)

    # Output final sorted list
    print("Sorted data:", data) # Sorted data: [12, 34, 64]
