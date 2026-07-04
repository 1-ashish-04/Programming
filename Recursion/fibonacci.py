# fibo(5) --> first 5 fibonacci number --> 0, 1, 1, 2, 3

def fibo(n):
    if n == 0  or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = 5
print(f"First {n} fibonacci number are: ")
for i in range(n):
    print(fibo(i), end=" ")

print(f"Sum of first {n} fibonacci number is: {fibo(n)}")