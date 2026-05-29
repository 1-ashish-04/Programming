# Minimum Element After Replacement With Digit sum

# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.

# Example 1:

# Input: nums = [10,12,13,14]

# Output: 1

# Explanation:

# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 1

# Explanation:

# nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

class Solution:
    def minElement(self, nums):
        minSum = float('inf')
        for i in nums:
            sum = 0
            while(i):
                r = i % 10
                i = i // 10
                sum += i
                minSum = min(minSum, sum)
        return minSum

s = Solution()
print(s.minElement([10,12,13,14]))