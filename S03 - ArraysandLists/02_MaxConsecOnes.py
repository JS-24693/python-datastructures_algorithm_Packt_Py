from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        currentCount = 0

        for num in nums:
            if num == 1:
                currentCount += 1
                if currentCount > ans:
                    ans = currentCount
            else:                    # reset counter to 0
                currentCount = 0
        return ans

# instantiate and test
s = Solution()

print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))     # 3
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))     # 2
print(s.findMaxConsecutiveOnes([0,0,0]))           # 0
print(s.findMaxConsecutiveOnes([1,1,1,1]))         # 4
