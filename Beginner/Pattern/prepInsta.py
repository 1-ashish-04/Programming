# 10 
# 9 8 
# 7 6 5 
# 4 3 2 1 

# n = 4

# count = 0

# for i in range(1, n+1):
#     count += i

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(count, end=" ")
#         count -= 1
#     print("")

# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 

# n = 4
# m = 6
# for i in range(1, n+1):
#     for j in range(1,m+1):
#         print("*", end=" ")
#     print("")

# ******
# *    *
# *    *
# ******

# n = 4
# m = 6
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if (i == 1 or i == n or j == 1 or j == m):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")


#       * 
#     *   * 
#   *       * 
# * * * * * * * 

# n = 4
# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end=" ")

#     for j in range(1, i+i):
#         if (j == 1 or j == i+i-1 or i == n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
        
#     print("")

# * * * * * * * 
#   *       * 
#     *   * 
#       * 

# n = 4
# for i in range(1, n+1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for j in range(1, n-i+n-i+2):
#         if(i == 1 or j ==1 or j == n-i+n-i+1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# 3 
# 4 5 
# 6 7 8 
# 9 10 11 12 

# count = 3
# n = 4 
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(count, end=" ")
#         count += 1
#     print("")

# 3
# 44
# 555
# 6666

# count = 3
# n = 4
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(count, end="")
#     count += 1
#     print("")

# 6666
# 555
# 44
# 3

# count = 0
# n = 4
# for i in range(1,n):
#     count += i

# for i in range(1, n+1):
#     for j in range(1,n-i+2):
#         print(count, end="")
#     count -= 1
#     print("")