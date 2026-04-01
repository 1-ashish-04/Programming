
# Optimisation of insertion and accessing the elements  using HashMap

# 287. Find the Duplicate Number

a = [1,2,3,4,2]

# Using BruteForce

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if(a[i] == a[j]):
#             print(a[i])

# Using HashMap

# h = {}
# for i in a:
#     if(i in h.keys()):
#         print(i)
#         h[i] += 1
#     else:
#         h[i] = 1
    

# Using set

# s = set()
# for i in a:
#     if(i in s):
#         print(i)
#     else:
#         s.add(i)
