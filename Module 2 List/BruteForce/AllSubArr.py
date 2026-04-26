arr = [10,20,30,40,50]

# 1 . Print all subarray of the given array
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         for k in range(i,j+1):
#             print(arr[k], end=" ")
#         print()
    
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         #print(i,j, end="\n")
        
#         for k in range(i,j+1):
#             print(arr[k], end=" ")
#         print()

# 2 print sum of all the sub array

# sum = 0
# totalSum = 0
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         for k in range(i,j+1):
#             sum += arr[k]
#             print(arr[k], end=" ")
#         print(" --> Result -->",sum, end=" ")
#         totalSum += sum
#         sum = 0
#         print()
# print("Overall sum of all the sub array-->", totalSum)

# 3. count all the subArray with sum == target

# target = 50
# sum = 0
# count = 0
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         for k in range(i, j+1):
#             sum += arr[k]
#         if(sum == target):
#             count += 1

#         sum = 0
# print(count)

# using these slicing method we can print the subarray of the given array , but with it can't print the sum of the subarray
# for that we have to use 3 for loop approach.

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j+1], end=" ")
    print()
