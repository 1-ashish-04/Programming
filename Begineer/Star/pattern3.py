n = 5

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print("")

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("")

# for i in range(1, n+1, 1):
#     y = 5  # always use extra variable to print the output
#     for j in range(1, i+1):
#         print(y, end="")
#         y -= 1
#     print("")

# alternative

# for i in range(n , 0, -1):
#     for j in range(n, i-1 , -1):
#         print(j, end="")
#     print("")

# c = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(c, end=" ");
#         c += 1
#     print("")

# y = 15
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(y, end=" ")
#         y -= 1
#     print("")

# y = 1
# for i in range(1, n+1):

#     for j in range(1, n-i+1):
#         print(" ", end="")
    
#     for j in range(1, i+ i):
#         if( i == j):
#             print(i, end="")
#         elif (j <= i):
#             print(y, end="")
#             y += 1
#         else:
#             y -= 1
#             print(y, end="")
            
#     print("")

# alternative

# for i in range(1, n+1):

#     for j in range(1, n-i+1):
#         print(" ", end="")

#     y = 1
#     for j in range(1, i+1):
#         print(y, end="")
#         y+=1

#     y = i-1
#     for j in range(1, i):
#         print(y, end="")
#         y -= 1
            
#     print("")

 
# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
    
#     y = i
#     for j in range(1, i+1):
#         print(y, end = "")
#         y -= 1

#     y = 2
#     for j in range(1, i-1):
#         print(y, end="")
#         y += 1

#     print("")

# alternative

# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(" ", end="")

#     y = i
#     for j in range(1, i+i):
#         if (i == j):
#             print(y, end="")
#         elif (j< i):
#             print(y, end="")
#             y -= 1
#         else:
#             y+= 1
#             print(y, end="")
         
#     print("")


# 111111111
# 122222221
# 123333321
# 123444321
# 123454321
# 123444321
# 123333321
# 122222221
# 222222222



# for i in range(1, n+1):
#     for j in range(1, i):
#         print(j, end="")
   
#     for j in range(1, n-i+n-i+1+1):
#         print(i, end="")
#     y = i - 1
#     for j in range(1, i):
#         print(y, end="")
#         y -= 1
#     print("")

# for i in range(1, n):
#     for j in range(1, n-i):
#         print(j, end="")

#         y = n-i
#     for j in range(1, i+i+2):
#         print(y, end="")

#         y1 = n -1- i
#     for j in range(1, n-i):
#         print(y1, end="")
#         y1 -= 1
#     print("")

# altermnative

# for i in range(1, n+1):
#     y = 1
#     for j in range(1,i):
#         print(y, end="")
#         y += 1

#     y = i
#     for j in range(1, n-i+n-i+1+1):
#         print(y, end="")

#     y1 = i-1
#     for j in range(1, i):
#         print(y1, end="")
#         y1 -= 1
#     print("")

# n = 4
# for i in range(1, n+1):
#     y = 1
#     for j in range(1, n-i+1):
#         print(y, end="")
#         y += 1

#     y = n-i+1   
#     for j in range(1, i+i+2):
#         print(y, end="")
#     y = n-i
#     for j in range(1,n-i+1):
#         print(y, end="")
#     print("")
