

def firstNaturalNo(n):
    a = [0] * n
    a[0] = 1
    for i in range(1, n,1):
        a[i] = a[i-1] + 1
    return a

x = firstNaturalNo(10)
print(x)