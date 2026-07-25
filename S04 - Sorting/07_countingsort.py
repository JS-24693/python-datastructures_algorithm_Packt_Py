class CountingSort:
    @staticmethod
    def sort(arr):
        """
        Perform counting sort on list arr.
        Steps:
            1. Build frequency array of size (max_value + 1)
            2. Convert frequency array to cumulative frequency
            3. Traverse arr in reverse to ensure stability
            4. Place each element into its correct sorted position
            5. Copy result back into arr
        Time complexity: O(n + m)
        Space complexity: O(n + m)
        """
        if not arr:
            return arr

        # 1. Find max element
        max_val = max(arr)

        # 2. Build frequency array
        freq = [0] * (max_val + 1)
        for num in arr:
            freq[num] += 1

        # 3. Build cumulative frequency
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        # 4. Build output array (stable: traverse arr in reverse)
        temp = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            x = arr[i]
            pos = freq[x] - 1
            temp[pos] = x
            freq[x] -= 1

        # 5. Copy back
        for i in range(len(arr)):
            arr[i] = temp[i]

        return arr

# Test instantiation
if __name__ == "__main__":
    arr = [5, 1, 2, 3, 4, 6, 5, 2]
    print("Before sorting:", arr)
    CountingSort.sort(arr)
    print("After sorting :", arr)

# Before sorting: [5, 1, 2, 3, 4, 6, 5, 2]
# After sorting : [1, 2, 2, 3, 4, 5, 5, 6]
