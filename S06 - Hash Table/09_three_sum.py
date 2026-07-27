from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique triplets [a, b, c] such that a + b + c = 0.

        Approach:
        - Sort nums.
        - For each index i, treat nums[i] as the first element.
        - Use a two-pointer twoSum on the subarray i+1..n-1 to find pairs
          whose sum equals -nums[i].
        - Skip duplicates for both the first element and pointer elements.

        Time: O(N^2)
        Space: O(N) for storing triplets
        """
        nums.sort()
        n = len(nums)
        ans = []
        i = 0

        while i < n:
            # Skip duplicate first elements
            if i == 0 or nums[i] != nums[i - 1]:
                first = nums[i]
                target = -first
                pairs = self.twoSum(nums, i + 1, n - 1, target)

                for p in pairs:
                    ans.append([first, p[0], p[1]])

            i += 1

        return ans

    def twoSum(self, nums, start, end, target):
        """
        Two-pointer search for pairs in nums[start..end] whose sum = target.
        Skips duplicates to ensure unique pairs.
        """
        f = start
        s = end
        pairs = []

        while f < s:
            # Skip duplicate left pointer values
            if f - 1 >= start and nums[f] == nums[f - 1]:
                f += 1
                continue

            # Skip duplicate right pointer values
            if s + 1 <= end and nums[s] == nums[s + 1]:
                s -= 1
                continue

            curr = nums[f] + nums[s]

            if curr < target:
                f += 1
            elif curr > target:
                s -= 1
            else:
                pairs.append([nums[f], nums[s]])
                f += 1  # move forward to find next unique pair

        return pairs

# Test Instantiation
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    result = sol.threeSum(nums)

    print("Input nums:", nums)         # Input nums: [-4, -1, -1, 0, 1, 2]
    print("Three Sum result:", result) # Three Sum result: [[-1, -1, 2], [-1, 0, 1]]
