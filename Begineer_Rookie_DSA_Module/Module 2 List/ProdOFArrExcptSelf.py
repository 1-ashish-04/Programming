# Product of Array Excpet Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def product(self, nums):
        # calculating product of array from 0 index (starting) (left to right)
        prefixProd = [0] * len(nums) 
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            prefixProd[i] = prod
        # calculating product of array from last index (right to left)
        suffixProd = [0] * len(nums)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            suffixProd[i] = prod
        # store the product of arr for 0 and last index (in which these index value is not included)
        nums[0] = suffixProd[1]
        nums[-1] = prefixProd[-2]
        # if size of arr is 2 then return nums as already we pass the value for index 0 and -1
        if len(nums) == 2:
            return nums
        # insert the product of arr for remaining index
        for i in range(1, len(nums)-1):
            nums[i] = prefixProd[i-1] * suffixProd[i+1]
        return nums

s = Solution()

print(s.product([1,2,3,4,5]))