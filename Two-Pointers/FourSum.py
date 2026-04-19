# Four Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

# Sort the array using Two Pointer

# Approach
# fix the i and j and change the k and l
# [i  j    k....................l]


def FourSum(nums, target):
    nums.sort()
    s = set()
    for i in range(len(nums)-3): # as go maximum to -4 index from last as quadraple needed
        for j in range(i+1, len(nums)-2): # got to maximum till -3 from last
            k = j+1
            l = len(nums)-1
            while(k < l):
                result = nums[i] + nums[j] + nums[k] + nums[l]
                if result == target: # If equal to target
                    s.add(tuple([nums[i], nums[j], nums[k], nums[l]])) # add to set s
                    k += 1  #  change the index
                    l -= 1
                elif result > target:
                    l -= 1
                else:
                    k += 1
    return [list(i) for i in s]

r = FourSum([1,0,-1,0,-2,2], 0)
print(r)

def fourSum2(nums, target):
    nums.sort()
    s = set()
    i = 0
    while(i < len(nums)-3):
        j = i + 1
        while(j < len(nums)-2):
            k = j+1
            l = len(nums)-1
            while(k < l):
                result = nums[i] + nums[j] + nums[k] + nums[l]
                if result == target:
                    s.add(tuple([nums[i], nums[j], nums[k], nums[l]]))
                    k += 1
                    l -= 1
                elif result > target:
                    l -= 1
                else:
                    k += 1
            j += 1 # After innermost loop increase the j (index value), means second value of the quadraple
        i += 1 # And after middle loop incease i , first value of the quadraple
    return [list(i) for i in s]

print(fourSum2([1,0,-1,0,-2,2], 0))