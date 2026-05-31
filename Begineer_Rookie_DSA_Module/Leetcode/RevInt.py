# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

class Solution:
    def reverse(self, n):
        negative = False
        if n < 0:
            n = abs(n)
            negative = True
        result = 0
        while(n):
            r = n % 10
            n = n // 10
            result = (result * 10) + r
        if negative == True:
            result = result * (-1)
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result

s = Solution()
print(s.reverse(12))

print(s.reverse(-123))