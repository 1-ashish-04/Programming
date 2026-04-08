# optimisation in arrays : HashMap or Hashset  (Always think these first)

# Two Sum Optimization using hashmap  ( two sum == k)

# Time complexity --> O(n)
class TwoSum:
    def solution(self, a, k):
        h = {}
        x = 0  # Tracking index of the given array
        # for i in a: # Using for each loop
        #     if ((k - i) in h):            # x + y == k -->  k - y == x --> k - i == x (value present in hashmap)
        #         return [h[k - i]  , x]   
        #     h[i] = x   # Insert into hashmap
        #     x += 1 
        # return 

        for i in range(len(a)):  # using for loop
            if ((k - a[i]) in h):   # x + y == k -->  k - y == x --> k - a[i] == x (value present in hashmap)
                return [ h[k - a[i]], i]
            h[i] = i
 
t = TwoSum()

result = t.solution([2,3,4,5,6,7,8], 8)

print(result)

result = t.solution([2,3,4,5,6,7,8], 0)

print(result)