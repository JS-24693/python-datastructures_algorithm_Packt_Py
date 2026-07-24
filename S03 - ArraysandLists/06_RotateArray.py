# 06_RotateArray.py

from typing import List

class Solution:
    """
    Rotate an array nums to the right by k steps using O(n) time.
    The rotation is performed by reversing segments of the list.
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Reverse the entire list, then reverse the first k elements,
        then reverse the remaining n - k elements.
        """
        n = len(nums)
        if n == 0:
            return

        k %= n  # normalize k

        # full reverse
        self.reverse(nums, 0, n - 1)
        # reverse first k
        self.reverse(nums, 0, k - 1)
        # reverse remaining n - k
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """
        In-place reverse of nums[start:end] inclusive.
        """
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

# Test instantiations
s = Solution()

arr1 = [1,2,3,4,5,6,7]
s.rotate(arr1, 3)
print(arr1)        # [5,6,7,1,2,3,4]

arr2 = [-1,-100,3,99]
s.rotate(arr2, 2)
print(arr2)        # [3,99,-1,-100]

arr3 = [10,20,30,40]
s.rotate(arr3, 1)
print(arr3)        # [40,10,20,30]
