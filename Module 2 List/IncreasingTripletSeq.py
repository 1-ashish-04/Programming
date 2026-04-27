# Increasing Triplet Sequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

def incTripSeq(nums):
    if len(nums) < 3 : # If length of given arr is less then 3 then no such triplet seq possible
        return False
    
    pre = [0]*len(nums) # Store the prefix (minimum value from the starting to the last) for each index
    pre[0] = nums[0] #  by default give same value to the zero index as present in arr
    for i in range(1, len(nums)): # then comparing minimum value to the remaining index
        pre[i] = min(pre[i-1], nums[i])
    
    suf = [0] * len(nums) # Store the suffix (maximum value from the last to the starting) for each index
    suf[len(suf)-1] = nums[len(nums)-1] #  by default give same value to the last index as present in arr
    for i in range(len(nums)-2, -1, -1): # then comparing maximum value to the remaining index
        suf[i] = max(suf[i+1], nums[i])

    for i in range(1, len(nums)-1):
        if i > pre[i-1] and i < suf[i+1]: # check triplet seq such that -> current value present in nums (arr) greater then the value present in pre[i-1] (prefix arr of the current index -1 [one previous index]) and less then value present in suf[i+1] (suffix arr of the current index+1 [one next index]) 
            return True
    return False

result = incTripSeq([1,4,2,0,5,43,5])
print(result)
 
def incTripSeq2(nums):
    if len(nums) < 3:
        return False
    # Create two variable  store minimum and middle value for triplet seq and with there help find max value from both --->   mini --> middle --> maximum
    mini = float('inf')
    middle = float('inf')
    for i in nums:
        if mini >= i:
            mini = i
        elif middle >= i:
            middle = i
        else:
            return True
    return False

print(incTripSeq2([1,4,2,0,5,43,5]))
