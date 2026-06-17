# A is said to be factore of B
# if B % A == 0 True

def isFactor(a,b):
    if b % a == 0:
        return True
    return False

print(isFactor(20,4))
print(isFactor(5, 10))