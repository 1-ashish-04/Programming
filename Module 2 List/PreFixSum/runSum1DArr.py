#Running sum of 1D Array[leetCode]

a = [1,2,4,6,8,10]
prefixSumA = [0 for i in range(len(a))]
sum = 0
for i in range(len(a)):
    sum += a[i]
    prefixSumA[i] += sum

print("******** a List *********")
print(a)
print("******** Running sum of list a *******")
print(prefixSumA)