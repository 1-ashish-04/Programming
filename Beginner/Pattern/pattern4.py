n = 9

# *********
# *       *
# *       *
# *       *
# *       *
# *       *
# *       *
# *       *
# *********

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if (i == 1 or i == n or j == 1 or j ==n):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")


# *********
# **      *
# * *     *
# *  *    *
# *   *   *
# *    *  *
# *     * *
# *      **
# *********

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == 1 or i == n or j == 1 or j ==n or i == j):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")


# *********
# *      **
# *     * *
# *    *  *
# *   *   *
# *  *    *
# * *     *
# **      *
# *********

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == 1 or i == n or j == 1 or j ==n or i + j == n+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")


# *       *
#  *     * 
#   *   *  
#    * *   
#     *    
#    * *   
#   *   *  
#  *     * 
# *       *

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == j or i + j == n+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

# *        
# **       
# * *      
# *  *     
# *   *    
# *    *   
# *     *  
# *      * 
# *********

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == j or j == 1 or i == n):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

# *********
# *      * 
# *     *  
# *    *   
# *   *    
# *  *     
# * *      
# **       
# *

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == 1 or j == 1 or i+j == n+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")


#         *
#        **
#       * *
#      *  *
#     *   *
#    *    *
#   *     *
#  *      *
# *********

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == n or j == n or i+j == n+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

# *********
#  *     * 
#   *   *  
#    * *   
#     *    
#    * *   
#   *   *  
#  *     * 
# *********

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i == n or i == 1 or i == j or i+j == n+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

# *       *
# **     **
# * *   * *
# *  * *  *
# *   *   *
# *  * *  *
# * *   * *
# **     **
# *       *

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(j == n or j == 1 or i == j or i+j == n+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

#     *    
#    * *   
#   *   *  
#  *     * 
# *       *
#  *     * 
#   *   *  
#    * *   
#     *  

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if( i + j + 4== n+1 or i + j  == n + 1 + 4  or i == j - 4 or i == j + 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")