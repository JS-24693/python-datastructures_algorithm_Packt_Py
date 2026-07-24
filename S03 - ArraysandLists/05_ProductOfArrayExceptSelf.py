from typing import List

class Solution:
    """
    Return an array where each element is the product of all other elements
    except itself, computed without using division.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Build prefix (left) and suffix (right) products, then multiply them
        to produce the final output.
        """
        left = [1]                 # prefix products
        n = len(nums)

        # build left products: product of all values before index i
        for i in range(1, n):
            left.append(left[i-1] * nums[i-1])

        right = [1] * (n + 1)      # suffix products (one extra for boundary)

        # build right products: product of all values after index i
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        output = []

        # each position = left product * right product
        for i in range(n):
            output.append(left[i] * right[i])

        return output

# instantiate and test
s = Solution()

print(s.productExceptSelf([1,2,3,4]))          # [24,12,8,6]
print(s.productExceptSelf([2,3,4,5]))          # [60,40,30,24]
print(s.productExceptSelf([5,1,10,2]))         # [20,100,10,50]
