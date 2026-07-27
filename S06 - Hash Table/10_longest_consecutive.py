from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Return the length of the longest consecutive integer sequence.

        Approach:
        - Insert all numbers into a set for O(1) membership checks.
        - For each number, check if it is the start of a sequence
          (i.e., num - 1 is not in the set).
        - If it is a start, count upward until the sequence ends.
        - Track the maximum streak length.

        Time: O(N)
        Space: O(N)
        """
        nSet = set(nums)
        ans = 0

        for num in nums:
            # Only start counting if num is the beginning of a sequence
            if num - 1 not in nSet:
                current = num
                currentStreak = 1

                # Count forward while consecutive numbers exist
                while current + 1 in nSet:
                    current += 1
                    currentStreak += 1

                # Update longest streak
                if currentStreak > ans:
                    ans = currentStreak

        return ans

# Test Instantiation
if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0]
    sol = Solution()
    result = sol.longestConsecutive(nums)

    print("Input nums:", nums) # Input nums: [0, 3, 7, 2, 5, 8, 4, 6, 0]
    print("Longest consecutive sequence length:", result) 
    # Longest consecutive sequence length: 7
