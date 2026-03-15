n = 5
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1, n+1):
#     y = i
#     for j in range(1, i+1):
#         print(y , end="")
#     print("")


# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         y = j
#         print( y, end="")
#     print("")

# 5
# 44
# 333
# 2222
# 11111

# for i in range(1, n+1):
#     y = n-i+1
#     for j in range(1, i+1):
#         print( y, end="")
#     print("")


# 5
# 45
# 345
# 2345
# 12345

# for i in range(1, n+1):
#     y = n-i+1
#     for j in range(1, i+1):
#         print( y , end="")
#         y += 1
        
#     print("")


# 5
# 54
# 543
# 5432
# 54321

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         y = n-j+1
#         print( y , end="")
        
#     print("")

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# y =  1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(y , end="")
#         y += 1
#     print("")

# 1          ------------------------------------------ incomplete
# 3 2
# 6 5 4
# 10 9 8 7 

# y = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if (i % 2 == 0):

#             print( y, end="")
#             y -= 1
#         else:
#             print(y, end="")
#             y -= 1
#     print("")


#     1
#    121
#   12321
#  1234321
# 123454321

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")

#     for j in range(1, i+1):
#         y = j
#         print( y, end="")
#     y = i-1
#     for j in range(1, i):
        
#         print(y, end="")
#         y -= 1
#     print("")

#     1
#    212 
#   32123
#  4321234
# 543212345

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")

#     y = i
#     for j in range(1, i+1):
#         print(y, end="")
#         y -= 1
        
#     y = 2
#     for j in range(1,i):
#         print(y, end="")
#         y += 1
#     print("")


#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1


# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
    
#     for j in range(1, i+1):
#         print(j, end="")

#     y = i -1
#     for j in range(1, i):
#         print(y, end="")
#         y -= 1
#     print("")

# n = 4

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(" ", end="")
    
#     for j in range(1, n-i+2):
#         print(j, end="")
#     y =n-i
#     for j in range(1, n-i+1):
#         print(y, end="")
#         y -= 1
#     print("")

# 111111111
# 122222221
# 123333321
# 123444321
# 123454321
# 123444321
# 123333321
# 122222221
# 111111111

# for i in range(1, n+1):
#     for j in range(1,i):
#         print(j, end="")
#     for j in range(1, n-i+n-i+2):
#         print(i, end="")
        
#     y = i -1
#     for j in range(1, i):
#         print(y, end="")
#         y -= 1
#     print("")

# n = 4
# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(j, end="")

#     y = n -i +1
#     for j in range(1, i+i+1):
#         print(y, end="")

#     y = n-i
#     for j in range(1, n-i+1):
#         print(y, end="")
#         y -= 1
#     print("")

        