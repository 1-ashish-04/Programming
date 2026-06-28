# Find First And Last Position Of Element in sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:

    def bruteForce(self, nums, k):
        left = -1
        right = -1
        for i in range(len(nums)):
            if nums[i] == k:
                if left == -1:
                    left = i
                right = i
        return [left, right]
    

    # using two binary search one track left most, while other right most
    def searchRange(self, nums, k):
        left = -1
        right = -1

        i = 0
        j = len(nums)-1

        while(i <= j):
            mid = i + (j-i)//2
            if k == nums[mid]:
                left = mid
                j = mid - 1
            elif k > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1

        i = 0
        j = len(nums)-1

        while(i <= j):
            mid = i + (j-i)//2
            if k == nums[mid]:
                right = mid
                i = mid + 1
            elif k > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return [left, right]



s = Solution()

x = s.searchRange([5,7,7,8,8,10], 8)
print(x)