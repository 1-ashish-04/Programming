n = 5

# *****
# *****
# *****
# *****
# *****

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("*",end="")
#     print("")

# 12345
# 12345
# 12345
# 12345
# 12345

# for i in range(1,n+1):
#     for j in range(1, n+1):
#         print(j,end="")
#     print("")

# 11111
# 22222
# 33333
# 44444
# 55555

# for i in range(1,n+1):
#     for j in range(1, n+1):
#         print(i,end="")
#     print("")


# *
# **
# ***
# ****
# *****

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("")


# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print("")


# ******
# *****
# ***
# **
# *

# for i in range(1,n+1):
#     for j in range(1,n-i+1+1):
#         print("*",end="")
#     print("")

# 11111
# 2222
# 333
# 44
# 5

# for i in range(1,n+1):
#     for j in range(1,n-i+1+1):
#         print(j,end="")
#     print("")

# *
# ***
# *****
# *******
# *********

# for i in range(1,n+1):
#     for j in range(1,i+i-1+1):
#         print("*",end="")
#     print("")

# *********
# *******
# *****
# ***
# *

for i in range(1,n+1):
    for j in range(1,n-i+n-i+1+1):
        print("*",end="")
    print("")