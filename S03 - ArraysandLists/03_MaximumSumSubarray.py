class MaximumSum:
    """
    Implements the maximum subarray sum algorithm (Kadane's Algorithm).
    Computes the largest possible sum of any contiguous subarray.
    """

    def max_subarray(self, nums):
        """
        Return the maximum subarray sum for the input list nums.
        Runs in O(n) time and O(1) extra space.
        """
        current = 0          # running best sum ending at current index
        best = float('-inf') # global best sum seen so far

        for x in nums:
            # either extend the previous subarray or start a new one at x
            current = max(x, current + x)

            # update global best if current is larger
            best = max(best, current)

        return best

# Test Instantiation
ms = MaximumSum()

result = ms.max_subarray([1, -2, 3, 5, -1, 2])
print(result)   # 9

result2 = ms.max_subarray([-5, -1, -8])
print(result2)  # -1

result3 = ms.max_subarray([7, -2, 5, -1, 6])
print(result3)  # 15