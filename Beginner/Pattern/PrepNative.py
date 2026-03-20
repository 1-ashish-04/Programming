# 12345
# 22345
# 33345
# 44445
# 55555

# n = 5

# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if(j <= i):
#             print(i, end="")
#         else:
#             print(j, end="")
#     print("")

# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 20 25 
# 6 12 18 24 30 36 
# 7 14 21 28 35 42 49 
# 8 16 24 32 40 48 56 64 

# n = 8
# for i in range(1, n+1):
#     y = i
#     for j in range(1, i+1):
#         y *= j
#         print(y, end=" ")
#         y = i

#     print("")

# alternative

# for i in range(1, n+1):
    
#     for j in range(1, i+1):
#         y = i*j
#         print(y, end=" ")
#     print("")

# 14 
# 14 12 
# 14 12 10 
# 14 12 10 8 
# 14 12 10 8 6 
# 14 12 10 8 6 4 
# 14 12 10 8 6 4 2 

# n = 7
# for i in range(1, n+1):
#     y = n * 2
#     for j in range(1, i+1):
#         print(y, end=" ")
#         y -= 2
#     print("")

# 0 
# 0 1 
# 0 2 4 
# 0 3 6 9 
# 0 4 8 12 16 
# 0 5 10 15 20 25 
# 0 6 12 18 24 30 36 

# n = 7
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         y = (i-1) * (j - 1)
#         print(y, end=" ")
#     print("")


# 1 * 2 * 3 * 4 
# 1 * 2 * 3 
# 1 * 2 
# 1 

# n = 4

# for i in range(1, n+1):
#     y = 1
#     for j in range(1, n-i+n-i+2):
#         if( j % 2 != 0):
#             print(y, end=" ")
#             y += 1
#         else:
#             print("*", end=" ")
#     print("")

# 0 
# 4 8 
# 8 16 16 
# 16 32 32 32 

# n = 4
# y  = 0
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(y, end=" ")
#         y =    2 ** (i +1)
#     print("")

# 1 
# 2 1 
# 4 2 1 
# 8 4 2 1 
# 16 8 4 2 1 

# n = 4
# y = 1
# for i in range(1, n+1):
   
#     for j in range(1, i+1):
#         print(y, end=" ")
#         y //= 2
#     y = 2 ** i

#     print("")

# # alternative

# n = 4 
# for i in range(1, n+1):
#     y = 2 ** (i-1)
#     for j in range(1, i+1):
#         print(y, end=" ")
#         y //= 2
    
#     print("")