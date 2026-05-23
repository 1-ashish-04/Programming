class SuccessiveCal:

    def sucCal(self, n):
        sum = 0 
        for i in range(1, n+1):
            sum += i
        return sum

s = SuccessiveCal()
print(s.sucCal(6))
