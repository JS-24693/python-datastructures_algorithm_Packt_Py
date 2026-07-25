from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

def majority_element(nums):
    """
    Return the majority element using Moore's Voting Algorithm.
    Majority element is guaranteed to exist (appears > n/2 times).

    Algorithm:
        - Start with first element as candidate.
        - Increase count when element matches candidate.
        - Decrease count when element differs.
        - When count reaches zero, choose new candidate.
        - Final candidate is the majority element.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    candidate = nums[0]
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1

    return candidate

# Test instantiation
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 2, 2, 1]
    print("Array:", nums)
    print("Majority element:", majority_element(nums))

# Array: [2, 2, 1, 1, 2, 2, 1]
# Majority element: 2
