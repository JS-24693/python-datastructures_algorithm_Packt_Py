from typing import List

class Solution:
    """
    Compute the maximum subarray sum using Kadane's Algorithm.
    The method tracks a running sum and resets it when it becomes negative.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Iterate through nums, maintaining:
        - currentSum: best sum ending at the current index
        - maxSoFar: global maximum subarray sum seen so far
        """
        maxSoFar = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
            # reset running sum if it becomes negative
            if currentSum < 0:
                currentSum = 0

            # extend the current subarray
            currentSum += nums[i]

            # update global maximum
            if currentSum > maxSoFar:
                maxSoFar = currentSum

        return maxSoFar

# Test Instantiation
ms = Solution()

result = ms.maxSubArray([1, -2, 3, 5, -1, 2])
print(result)   # 9

result2 = ms.maxSubArray([-5, -1, -8])
print(result2)  # -1

result3 = ms.maxSubArray([7, -2, 5, -1, 6])
print(result3)  # 15