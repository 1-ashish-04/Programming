# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class MajorityElement:
    def solution(self, nums):
        n = len(nums)/2
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] > n:
                return i
        return -1

m = MajorityElement()
result = m.solution([3,2,3])

print(result)