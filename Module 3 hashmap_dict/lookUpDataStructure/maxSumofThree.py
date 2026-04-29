# print max sum of arr where i < j < k 
# and a[i] + a[j] + a[k] == max

# Approach --> Using Look up data structure
# from standing one place look side way
# from left and right max value for the current index value and store it into a list
# from that print the max result of sum

a = [1,2,-3,5,8,-11,2,3]

left = [0] * len(a)  # Finding the max value from the left side
left[0] = a[0]
for i in range(1, len(a)):
    left[i] = max(left[i-1], a[i])

right = [0] * len(a) # Finding the max value from the right side
right[-1] = a[-1]
for i in range( len(a)-2, -1, -1):
    right[i] = max(right[i+1], a[i])

print(a)
print(left)
print(right)

s = [0] * len(a) # calculate sum where i < j < k

for i in range(1, len(a)-1):
    s[i] = left[i-1] + a[i] + right[i+1]  

print(s)

print(max(s)) # Print max of sum
