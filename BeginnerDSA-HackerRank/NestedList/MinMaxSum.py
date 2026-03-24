class MinMax:

    def minMaxSum(self, li):
        # minSum = float('inf')
        # maxSum = 0
        # sum = 0
        # for i in range(len(li)):
        #     for j in range(len(li)):
        #         if(j == i):
        #             continue
        #         else:
        #             sum += li[j]
        #     if(maxSum < sum):
        #         maxSum = sum
        #     if(minSum > sum):
        #         minSum = sum
        #     sum = 0
        # print(minSum, maxSum)

        # alternate
        s = 0   # less time complexity
        for i in li:
            s += i
        print(s - max(li), s-min(li))

m = MinMax()
arr = [1,2,3,4,5]
m.minMaxSum(arr)