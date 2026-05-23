# Kadane's Algorithm ->  to find minimum sum of the subarray

a = [10, 20 , 10, -500, 10, 15 , -10, 10]

# a = [-100, 10, 20, 30, -500, 100, 10, -20, 10 ,10]

# a= [-100, -90, -80, -70, -60, - 50, -10]

pSum = 0
minSum = a[0]  # t handle the complete negative array
print(a)

for i in a:
    # pSum += i
    pSum = min(pSum + i , i)  # pSum + i  ,  i --> result comes which one is minimum
                              # --> 10 + 10, 10 -> 10
                              # --> 10 + 20 , 20 -> 20
                              # --> 20 + 10, 10 -> 10
                              # --> 10 + (-500) , -500 -> -500
                              # --> -500 + 10, 10 => -490
                              # --> -490 + 15, 10 -> -475
                              # --> -475 + (-10), -10 -> -485
                              # --> -485 + 10, 10 => -475
    minSum = min(pSum, minSum)
    print(pSum, end=" ")

print()
# print(pSum)
print("Minimum sum of the subArray is", minSum)