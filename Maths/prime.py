# method 1
# Time Complexity O(n)

# Check n is a prime or not
n = 7

def prime(n):
    if n <= 1:
        return "Not a prime number"
    for i in range(2,n):
        if n % i == 0:
            return "Not a prime number"
    return "Prime number"

print(prime(n))

# method 2 
# optimized using the sqrt(n)

def primeOptimized(n):
    if n <= 1:
        return "Not a prime number"
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return "Not a prime number"
    return "Prime number"

print(primeOptimized(n))