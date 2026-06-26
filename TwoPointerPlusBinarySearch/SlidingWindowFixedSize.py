# Maximum Sum of Subarrays With Length K

# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following condition:

#     The length of the subarray is k,

# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:

    # brute force approach O(n * k)
    def bruteSilding(self, nums, k):
        maximum = 0
        for i in range(len(nums)-k+1): # To restirct the last window of given k size
            sum = 0
            for j in range(i, k+i-1+1): # ensure after each loop window move forward by one
                sum += nums[j]
            maximum = max(maximum, sum)
        return maximum



    # Optimized time complexity --> O(n)  # note--> these is not the work if duplicate not conisder
    def optimizedSliding(self, nums, k):
        i = 0 
        j = 0
        sum = 0
        k = k-1
        while(j <= k):
            sum += nums[j]
            j += 1
        maximum = sum
        while(j < len(nums)):
            sum = sum - nums[i]
            i += 1
            sum += nums[j]
            j += 1
            maximum = max(maximum, sum)
        return maximum

s = Solution()
x = s.bruteSilding([1,5,4,2,9,9,9], 3)
print(x)

x = s.optimizedSliding([1,5,4,2,9,9,9], 3)
print(x)