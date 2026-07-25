from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros in nums to the end while preserving the relative
        order of non-zero elements. Operates in-place.

        Approach:
            - Maintain a pointer 'start' for the next non-zero placement.
            - Scan left-to-right.
            - When a non-zero is found, swap it with nums[start] and increment start.
            - Zeros naturally shift to the end.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        start = 0  # next position for a non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1

# Test Instantiation
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print("Before:", nums)

    s = Solution()        # Instantiation
    s.moveZeroes(nums)    # call method on instance

    print("After :", nums)

# Before: [0, 1, 0, 3, 12]
# After : [1, 3, 12, 0, 0]
