# Intersection of Two II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]


def InterSectionOfTwoArr(a,b):
    h = {} # Store the frequency of an element
    result = []
    for i in a:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
    
    for i in b: # Iterate over b
        if i in h and h[i] >= 1: # if i present in h.keys() and h.values() >= 1 then append
            result.append(i)
            h[i] -= 1 # and decrease the h.values()
    print(result)

InterSectionOfTwoArr([2,3,4,3,2], [2,3,2])