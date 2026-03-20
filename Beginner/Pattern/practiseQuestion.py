n = 5
# 1.

# *****
# *****
# *****
# *****
# *****

# for i in range(1, n+1):
#     for j in range(1,n+1):
#         print("*", end="")
#     print("")

# 2.

# *****
#  *****
#   *****
#    *****
#     *****

# for i in range(1, n+1):
#     for j in range(1, i):
#         print(" ", end="")
#     for j in range(1, n+1):
#         print("*", end="")
#     print("")

# 3.

#     *****
#    *****
#   *****
#  *****
# *****

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(1 , n+1):
#         print("*", end="")
#     print("")

# 4.

# *
# **
# ***
# ****
# *****

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("")


# 5.


#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(1,i+1):
#         print("*", end="")
#     print("")


# 6.

# *****
#  ****
#   ***
#    **
#     *

# for i in range(1, n+1):
#     for j in range(1,i):
#         print(" ", end="")
#     for j in range(1, n-i+1+1):
#         print("*", end ="")
#     print("")

# 7.

# *****
# ****
# ***
# **
# *

# for i in range(1, n+1):
#     for j in range(1, n-i+1+1):
#         print("*", end="")
#     print("")

# 8.

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for i in range(1, n+1):
#     for j in range(1 , i+1):
#         print("*", end="")
#     print("")
    
# for i in range(1 , n): # n-1+1
#     for j in range(1,n-i+1 ):
#         print("*", end="")
#     print("")

# 9.

#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print("")

# for i in range(1, n):
#     for j in range(1,i+1):
#         print(" ", end="")
#     for j in range(1, n-i+1):
#         print("*", end="")
#     print("")

# 10.

# *
# **
# ***
# ****
# *****
#  ****
#   *** 
#    **
#     *

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print("")

# for i in range(1, n):
#     for j in range(1,i+1):
#         print(" ", end="")
#     for j in range(1, n-i+1):
#         print("*", end="")
#     print("")

# 11.

#     *
#    **
#   ***
#  ****
# *****
# ****
# ***
# **
# *

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print("")

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print("*", end="")
#     print("")

# 12.


# *
# ***
# *****
# *******
# *********

# for i in range(1, n+1):
#     for j in range(1 , i+i):
#         print("*", end="")
#     print("")

# 13.

# **
# ****
# ******
# ********
# **********

# for i in range(1, n+1):
#     for j in range(1, i+i+1):
#         print("*", end="")
#     print("")

# 14.

# **********
# ********
# ******
# ****
# **

# for i in range(1, n+1):
#     for j in range(1, n-i+n-i+2+1):
#         print("*", end="")
#     print("")

# 15.

# *********
# *******
# *****
# ***
# *

# for i in range(1, n+1):
#     for j in range(1, n-i+n-i+1+1):
#         print("*", end="")
#     print("")

# 16.

#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(1, i+i-1+1):
#         print("*", end="")
#     print("")

# 17.

# *********
#  *******
#   *****
#    ***
#     *

# for i in range(1, n+1):
#     for j in range(1, i):
#         print(" ", end="")
#     for j in range(1, n-i+n-i+1+1):
#         print("*", end="")
#     print("")

# 18.


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(1, i+i):
#         print("*", end="")
#     print("")

# for i in range(1, n):
#     for j in range(1,i+1):
#         print(" ", end="")
#     for j in range(1,n-i+n-i):
#         print("*", end="")
#     print("")