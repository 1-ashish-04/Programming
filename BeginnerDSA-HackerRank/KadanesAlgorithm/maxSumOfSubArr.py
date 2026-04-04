a = [10, 20 , 10, -500, 10, 15 , -10, 10]

# a = [-100, 10, 20, 30, -500, 100, 10, -20, 10 ,10]

# a= [-100, -90, -80, -70, -60, - 50, -10]

pSum = 0
maxSum = a[0]  # t handle the complete negative array
print(a)

for i in a:
    # pSum += i
    pSum = max(pSum + i , i)  # pSum + i  ,  i --> result comes which one is greater/ maximum
                              # --> 10 + 10, 10 -> 10
                              # --> 10 + 20 , 20 -> 30
                              # --> 30 + 10, 10 -> 40
                              # --> 40 + (-500) , -500 -> -460
                              # --> -460 + 10, 10 => 10
                              # --> 10 + 15, 10 -> 25
                              # --> 25 + (-10), -10 -> 15
                              # --> 15 + 10, 10 => 25
    maxSum = max(pSum, maxSum)
    print(pSum, end=" ")

print()
# print(pSum)
print("Maximum sum of the subArray is", maxSum)