from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers whose sum equals the target.

        Uses a hash table mapping each seen number to its index.
        For each element nums[i], compute the complement (target - nums[i]).
        If the complement is already in the hash table, return the pair.

        Time: O(N)
        Space: O(N)
        """
        ht = {}  # number → index

        for i in range(len(nums)):
            x = nums[i]
            key = target - x
            print(f"i={i} → x={x} → need {key} →", end=" ")

            if key in ht:
                print(f"{key} found at index {ht[key]} → answer = [{ht[key]}, {i}]")
                # Problem guarantees exactly one solution
                return [ht[key], i]   # ht[key] = index of complement, i = index of current number

            print(f"not seen → store {x}:{i}")
            ht[x] = i 

# Example diagnostic trace (algorithm walkthrough)
# i=0 → x=5 → need 2 → not seen → store 5:0
# i=1 → x=4 → need 3 → not seen → store 4:1
# i=2 → x=6 → need 1 → not seen → store 6:2
# i=3 → x=8 → need -1 → not seen → store 8:3
# i=4 → x=3 → need 4 → 4 is in hash table at index 1 → answer = [1, 4]

# Test Instantiation
if __name__ == "__main__":

    nums = [5, 4, 6, 8, 3, 9]
    target = 7

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Input nums:", nums)       # Input nums: [5, 4, 6, 8, 3, 9]
    print("Target:", target)         # Target: 7
    print("Two Sum result, indices:", result) # Two Sum result, indices: [1, 4]
