# Given an integer array arr[]. Find the maximum sum of the subarray that starts and ends with the same value element. A single value subarray can be considered as the start and end with the same element.
# GFG Question

class Solution:
    def max_sum(self, arr):
        h = {}  # Tracking first time element comes index
        h2 = {} # If present one more time then it last appearance index storing
        x = 0 # zero based indexing used in hashmap

        for i in arr:
            if i in h: # If already present in h then store it into h2
                h2[i] = x
            else:  # If not present in h , then store it
                h[i] = x
            x += 1 # Increase each time over the arr

        if h2 == {}:  # If no element repeatina (All present single time)
            return max(arr)  # return the max value from the arr
        
        else:  # If value is repeating
            mSum = float('-inf')  # Store maxSum of the arr
            for i in h2: # iterate over h2

                start = h[i] # Start index of the arr
                end = h2[i]  # end index of the arr
                subArr = sum(arr[start : end+1]) # sum of the array
                mSum = max(mSum, subArr) # Comparission
            return mSum # return it

s = Solution()

r1 = s.max_sum([2,6,4])    
print(r1)

r2 = s.max_sum([6, 3, 2, 3, 2, 6])
print(r2)
        
                
           
                    
                
      
   