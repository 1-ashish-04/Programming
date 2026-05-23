# Factor b % a == 0

class Factor:
    def isAFactorofB(self, n):

        for i in range(1, n+1):
            if n % i == 0:
                print(f"{i} is the factor of {n}")

f = Factor()
f.isAFactorofB(10)