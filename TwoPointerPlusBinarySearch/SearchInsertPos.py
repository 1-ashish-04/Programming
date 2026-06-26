# Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:

    def searchInser(self, nums, target):
        i = 0
        j = len(nums)-1
        while(i <= j):
            mid = i + (j-i)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i

s = Solution()
x = s.searchInser([1,3,5,6], 5)
print(x)
