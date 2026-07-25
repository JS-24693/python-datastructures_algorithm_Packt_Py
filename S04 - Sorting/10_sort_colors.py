from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort an array containing only 0, 1, and 2 using the Dutch National Flag algorithm.
        Zeros move left, twos move right, ones remain in the middle.

        Pointers:
            left  -> next index where a 0 should be placed
            right -> next index where a 2 should be placed
            i     -> current scanning index

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:  # nums[i] == 1
                i += 1

# Test Instantiation
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 0, 1]
    print("Before:", nums)

    s = Solution()       # Instantiate variable
    s.sortColors(nums)   # call method on instance

    print("After :", nums)

# Before: [2, 0, 2, 1, 0, 1]
# After : [0, 0, 1, 1, 2, 2]

