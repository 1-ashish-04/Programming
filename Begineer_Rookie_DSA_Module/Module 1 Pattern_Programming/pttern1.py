# for i in range(5):
#     for j in range(5):
#         print("*", end="") 
#     print("")


# for i in range(1,6):   
#     for j in range(1,6):
#         print(i, end ="")
#     print("")

# for i in range(1,6):  
#     for j in range(1,6):
#         print(j, end="")
#     print("")

# ****************************************Incresing in Cutting Off Pattern **************
# generalization i + / - something   for j (second loop)

# for i in range(1,6):  
#     for j in range(1,i+1):
#         print("*", end="")
#     print("")

# for i in range(1,6):     
#     for j in range(1,i+2):
#         print("*", end="")
#     print("")

# increase in odd number

# for i in range(1,6):  # odd sequence
#     for j in range(1,i*2) :
#         print("*", end="") 
#     print("")  

# alternative

# for i in range(1,6):
#     for j in range(1, i + (i-1)+1,1):
#         print("*", end="")
#     print("")

# increasing even number

# for i in range(1,6):  # even number pattern
#     for j in range(1,i*2+1):
#         print("*", end="")
#     print("")

# alternative

# for i in range(1,6):
#     for j in range(1, i + i + 1):
#         print("*", end = "")
#     print("")

print("**********Phase 2*************\n")
# ****************************************Decreasing in Cutting Off Pattern **************
# generalization (n - i) + / - something   for j (second loop)

n = 5

# for i in range(1,n + 1):
#     for j in range(n, i-1, -1):
#         print("*", end="")
#     print("")

# alternative

# for i in range(n, 0,-1):
#     for j in range(i, 0, -1):
#         print("*", end = "")
#     print("")

# alternative

# for i in range(1,n+1,1):
#     for j in range(1, n-i+1+1, 1):
#         print("*", end="")
#     print("")


# decreasig odd number pattern

# for i in range(1, n+1,1):
#     for j in range(1, (n-i+1)+(n-i)+1, 1):
#         print("*", end="")
#     print("")

# decreasing even number pattern

# for i in range(1,n+1,1):
#     for j in range(1, n-i+n-i+2+1,1):
#         print("*",end="")
#     print("")