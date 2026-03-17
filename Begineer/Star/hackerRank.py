# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 

n = 4

for i in range(1, n+1):
    y = n
    for j in range(1, i):
        print(y, end=" ")
        y -= 1

    y = n - i+1
    for j in range(1, n-i+n-i+2):
        print(y, end=" ")

    for j in range(1, i):
        y = n - i + j +1
        print(y, end=" ")
    print("")

# n = 3
# for i in range(1, n+1):
#     y = n+1
#     for j in range(1, n-i+1):
#         print(y, end=" ") 
#         y -= 1
#     y = i+1
#     for j in range(1, i +i+2):
#         print(y, end=" ")

    
#     y = i + 2
#     for j in range(1, n-i+1):
    
#         print(y, end=" ")
#         y += 1
        
#     print("")