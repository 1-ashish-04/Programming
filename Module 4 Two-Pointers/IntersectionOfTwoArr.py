# Intersection Of Two Array

# Given two integer arrays nums1 and nums2, return an array of their . Each element in the result must be unique and you may return the result in any order.

class IntersectionOfTwoArr:
    def solution(self, nums1, nums2):
        s = set()  # Set to store the integer of an array
        result = [] # intersection result stored
        for i in nums1:
            s.add(i) # Add integer of nums1 into set s
        for i in nums2:
            if i in s and i not in result: # if i is present in s and not present in resulted array
                result.append(i) # then add it into the result list
        return result
    
i = IntersectionOfTwoArr()

result = i.solution([2,3,4,2,3], [2,3,2])
print(result)