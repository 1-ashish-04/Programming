# Time Complexity

# O(n) -->

n = 5

# for i in range(1, n+1):
#     print(i)

# n = 5  Loop run 5 time
# n = 100  Loop run 100 time
# n = 1000  Loop run 1000 time
# n = 200  Loop run 200 time

# O(n^2) 

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# i=1  ****** j runs 5 times 5
# i=2  ****** 5 times       5     
# i=3  ****** 5 times        5
# i=4  ****** 5 times        5  
# i=5  ****** 5 time        5 =25 times 

# 5 time * 5 times === 25
# n    *    n  === o(n^2)


# n  = 10

# for i in range(n):
#     for j in range(i+1, n):
#         print(j)

# i=1 j=2,3,4,5,6,7,8,9,10    9
# i=2 j=3,4,5,6,7,8,9,10        8
# i=3 j=4,5,6,7,8,9,10        7
# i=4 j=5,6,7,8,9,10        6
# i=5 j=6,7,8,9,10         5
# i=6 j=7,8,9,10          4
# i=7 j=8,9,10            3
# i=8 j=9,10              2
# i=9 j=10                1
# i=10 j=11 11<=10 (fail)

# 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0

# Total iterations = (n-1) + (n-2) + ... + 1 = n(n-1)/2

# (n^2 / 2) - (n / 2)

# (n^2 / 2)

# n^2

# time complexity --> O(n^2)

# O(n^3) 

# n = 5
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(k, end=" ")
#         print()

# i = 0 --> j = 0 --> 0 1 2 3 4  (5)
#           j = 1 --> 0 1 2 3 4  (5)
#           j = 2 --> 0 1 2 3 4  (5)
#           j = 3 --> 0 1 2 3 4  (5)
#           j = 4 --> 0 1 2 3 4  (5)

# i = 1 --> j = 0 --> 0 1 2 3 4  (5)
#           j = 1 --> 0 1 2 3 4  (5)
#           j = 2 --> 0 1 2 3 4  (5)
#           j = 3 --> 0 1 2 3 4  (5)
#           j = 4 --> 0 1 2 3 4  (5)


# i = 2 --> j = 0 --> 0 1 2 3 4  (5)
#           j = 1 --> 0 1 2 3 4  (5)
#           j = 2 --> 0 1 2 3 4  (5)
#           j = 3 --> 0 1 2 3 4  (5)
#           j = 4 --> 0 1 2 3 4  (5)


# i = 3 --> j = 0 --> 0 1 2 3 4  (5)
#           j = 1 --> 0 1 2 3 4  (5)
#           j = 2 --> 0 1 2 3 4  (5)
#           j = 3 --> 0 1 2 3 4  (5)
#           j = 4 --> 0 1 2 3 4  (5)


# i = 4 --> j = 0 --> 0 1 2 3 4  (5)
#           j = 1 --> 0 1 2 3 4  (5)
#           j = 2 --> 0 1 2 3 4  (5)
#           j = 3 --> 0 1 2 3 4  (5)
#           j = 4 --> 0 1 2 3 4  (5)

          