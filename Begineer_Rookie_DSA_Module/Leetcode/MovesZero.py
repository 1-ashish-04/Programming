# Moves Zero

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution:
    def movesZero(self, nums):
        i = 0 # track the zero's in an array
        for j in range(len(nums)):
            if nums[j] != 0: # if current index element in non zero then replace it and move i forward
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1
        return nums

s = Solution()
print(s.movesZero([0,1,0,3,12]))

# [0,1,0,3,12]
# i = 0 ,j = 0 --> nums[j] != 0 False
# i = 0 , j = 1 ---> nums[j] != 0 True [1,0,0,3,12] i+= 1
# i = 1, j = 2 ---> nums[j] != 0 False
# i = 1, j = 3 ---> nums[j] != 0 True [1,3,0,0,12] i+= 1
# i = 2, j = 4 ---> nums[j] != 0 True [1,3,12,0,0] i += 1
# loop exit
