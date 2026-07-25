class DivideAndConquer:
    @staticmethod
    def merge_sort(A, left, right):
        """
        Perform merge sort on list A between indices left and right (inclusive).
        Recursively divides the array into halves, sorts each half, and merges
        them using the merge() function.
        Time complexity: O(n log n)
        Space complexity: O(n)
        """
        if left >= right:
            return  # base case: one element

        mid = (left + right) // 2

        # divide step
        DivideAndConquer.merge_sort(A, left, mid)
        DivideAndConquer.merge_sort(A, mid + 1, right)

        # conquer step
        DivideAndConquer.merge(A, left, mid, right)

    @staticmethod
    def merge(A, start, mid, end):
        """
        Merge two sorted ranges of A:
            first:  start..mid
            second: mid+1..end
        Build temporary array C, then copy back into A.
        """
        i = start
        j = mid + 1
        C = []

        # merge while both halves have elements
        while i <= mid and j <= end:
            if A[i] <= A[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(A[j])
                j += 1

        # copy remaining left half
        while i <= mid:
            C.append(A[i])
            i += 1

        # copy remaining right half
        while j <= end:
            C.append(A[j])
            j += 1

        # copy merged result back into A
        for k in range(len(C)):
            A[start + k] = C[k]

# Test instantiation
if __name__ == "__main__":
    A = [7, 9, 3, 4, 1, 5, 10, 15, 12, 9, 18, 23, 14]
    print("Before sorting:", A)
    DivideAndConquer.merge_sort(A, 0, len(A) - 1)
    print("After sorting:", A) 
    
# Before sorting: [7, 9, 3, 4, 1, 5, 10, 15, 12, 9, 18, 23, 14]
# After sorting: [1, 3, 4, 5, 7, 9, 9, 10, 12, 14, 15, 18, 23]