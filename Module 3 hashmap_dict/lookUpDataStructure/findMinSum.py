# find sum of two integer from a list where i < j
# and sum is minimum from a list

# Approach --> Using look up data structure
# store the minimum valur from left of the given  list 
# and using that for current index find the min Value
# and store the result into another list
# and from that list print the min value

a = [1,2,-3,5,8,-11,2,3]

m = [0] * len(a)
m[0] = a[0]
for i in range(1,len(a)):
    m[i] = min(m[i-1], a[i])

print(a)
print(m)

s = [0] * len(a)
for i in range(1, len(a)):
    s[i] = a[i] + m[i-1]

print(s)
print(min(s))