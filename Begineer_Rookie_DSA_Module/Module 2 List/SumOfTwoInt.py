# Sum of Two Integer

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3

class SumOfTwoInt:
    def solution(self, a,b):
        return sum([a,b])
    
s = SumOfTwoInt()
print(s.solution(4,5))