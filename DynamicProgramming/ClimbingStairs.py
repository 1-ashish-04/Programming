# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


class ClimbingStairs:

    def climbingStair1(self, n): # space complexity = O(n)
        if n <= 2:
            return n
        d = [0] * n
        d[0] = 1
        d[1] = 2
        for i in range(2, n, 1):
            d[i] = d[i-1] + d[i-2]
        return d[-1]

    def climbingStair2(self, n): # space complexity = O(1)
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(2, n, 1):
            a,b = b , a + b
        return b
    
c = ClimbingStairs()

x = c.climbingStair1(10)
print(x)

y =  c.climbingStair2(10)
print(y)