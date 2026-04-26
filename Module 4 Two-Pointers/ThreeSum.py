# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets

def threeSum(nums):
    nums.sort()
    s = set()
    for i in range(len(nums)):
        j = i+1
        k = len(nums)-1
        while(j < k):
            if nums[i] + nums[j] + nums[k] == 0:
                s.add(tuple([nums[i], nums[j], nums[k]]))
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
    return [list(i) for i in s]

t = threeSum([-1,0,1,2,3,-2,2,0,1,-1,0,1,1,-2])
print(t)