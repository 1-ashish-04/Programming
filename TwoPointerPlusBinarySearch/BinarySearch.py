# Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
class Solution:
    def search(self, nums, target):
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return -1
    
    def search2(self, nums, target):
        i = 0
        j = len(nums)-1
        while i < j:
            mid = i + (j - i) // 2 # used when index is very large, to make it perform well, optimized it -> in ir=t the from i minus j and divide by 2 and that floor value is added to i to find mid value and it point to mid of that particular arr.
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return -1
    
s = Solution()

print(s.search([-1,0,3,5,9,12], 9))

print(s.search2([-1,0,3,5,9,12], 2))