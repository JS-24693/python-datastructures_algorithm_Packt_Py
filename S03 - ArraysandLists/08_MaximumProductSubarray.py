
from typing import List

class Solution:
    """
    Compute the maximum product of any contiguous subarray.
    Tracks both maxProduct and minProduct at each index because
    negative values can flip the sign and turn a minimum into a
    new maximum. Runs in O(n) time.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """
        Iterate through nums, updating:
        - maxProduct: maximum product ending at current index
        - minProduct: minimum product ending at current index
        Reset behavior occurs naturally when encountering zeros.
        """
        result = nums[0]
        maxProduct = nums[0]
        minProduct = nums[0]

        for i in range(1, len(nums)):
            # store previous max before overwriting
            if nums[i] >= 0:
                maxProduct = max(maxProduct * nums[i], nums[i])
                minProduct = min(minProduct * nums[i], nums[i])
            else:
                temp = maxProduct
                maxProduct = max(minProduct * nums[i], nums[i])
                minProduct = min(temp * nums[i], nums[i])

            # update global result
            result = max(result, maxProduct)

        return result

# Test Instantiation
s = Solution()

result1 = s.maxProduct([2, 3, -2, 4])
print(result1)   # 6

result2 = s.maxProduct([-2, 0, -1])
print(result2)   # 0

result3 = s.maxProduct([-2, -3, 7])
print(result3)   # 42

result4 = s.maxProduct([0, 2, -5, -2, 4, 0, 3, -1])
print(result4)   # 80

result5 = s.maxProduct([5])
print(result5)   # 5
