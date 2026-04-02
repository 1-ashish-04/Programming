
# q1. print true : if there is a subarray sum==k else false
# //subarray sum : prefix sum HashMap

a = [10, 40, 10 , 10,  80, -10, 10, 50, 10, 60, 10]

# for i in range(len(a)):   # Print all the subarray of the given array.
#         for j in range(i, len(a)):
#                 for k in range(i, j+1):
#                         print(a[k], end=" ")
#                 print()

h = {}
h[0] = 0
k = 70
sum = 0
x = 1
mark = 0

for i in a:
    sum += i
    if ((sum - k) in  h.values()):   # prefixSum[current] - prefixSum[alreadyPresent in Hashmap] == k
          print("True" )
          mark = 1
          break
    else:
          h[x] = sum
          x += 1
if (mark == 0):
     print("False")
print(a)
print(h)


