# Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # check for the 1 size array
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n == 0 or n == 1:
                    return True
                else:
                    return False
            else:
                if n == 0:
                    return True
                else:
                    return False
        # for other array
        for i in range(len(flowerbed)):
            # boundary condition
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 and n > 0:
                flowerbed[i] = 1
                n -= 1
            elif i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0 and n>0:
                flowerbed[i] = 1
                n -= 1
            elif i > 0 and i < len(flowerbed)-2 and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and n > 0:
                flowerbed[i] = 1
                n -= 1
        if n == 0:
            return True
        else:
            return False

s = Solution()

print(s.canPlaceFlowers([1,0,0,0,1], 1))