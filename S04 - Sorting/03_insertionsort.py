class AlgorithmConceptualUnderstanding:
    @staticmethod
    def insertion_sort(li):
        """
        Perform an in-place insertion sort on list `li`.
        Starting from index 1, treat li[0:i] as the sorted region.
        For each key = li[i], shift all elements greater than the key
        to the right, then insert the key at its correct position.
        Best case: O(n) when array is already sorted.
        Worst case: O(n^2) when many shifts are required.
        """
        n = len(li)

        for i in range(1, n):  # start from index 1 (index 0 is sorted)
            key = li[i]
            j = i - 1

            # shift elements greater than key to the right
            while j >= 0 and li[j] > key:
                li[j + 1] = li[j]
                j -= 1

            # insert key at correct position
            li[j + 1] = key

            # print insertion step
            print(f"Inserting {key} at index {j + 1}: {li}")

if __name__ == '__main__':
    data = [20, 40, 15, 5, 10]
    print("Before sorting:", data)
    AlgorithmConceptualUnderstanding.insertion_sort(data)
    print("Sorted data:", data)

# Before sorting: [20, 40, 15, 5, 10]

# Inserting 40 at index 1: [20, 40, 15, 5, 10]
# Inserting 15 at index 0: [15, 20, 40, 5, 10]
# Inserting 5 at index 0: [5, 15, 20, 40, 10]
# Inserting 10 at index 1: [5, 10, 15, 20, 40]

# Sorted data: [5, 10, 15, 20, 40]


