# find all the prime number between q and given number, and given number is excluded
# Given an integer n, return the number of prime numbers that are strictly less than n.

# Approach 1

# create an array of number size and initialize it with zero
# then for all non prime mark 1 and mark 0 for prime
# for index 0 and 1 mark 1 as they are not a prime
#  then iterate it and inner loop iteration start from i + i as iterate over the particular i table only, and increment the value by i after each inner loop iteration

def prime(n):
    if n <= 2:
        return 0
    p = [0] * n
    p[0] = p[1] = 1
    for i in range(2, n,1):
        for j in range(i + i, n, i):
            p[j] = 1
    print(p)
    c = 0
    for i in p:
        if i == 0:
            c += 1
    print(c)

prime(10)

# aproach 2

# create an array of number size and initialize it with True
# then for all non prime mark False and mark 0 for True
# for index 0 and 1 mark False as they are not a prime
# the outer loop iterate till sqrt(n) as till it cover all the cases,
# and then iterate  inner loop, iteration start from i * i as All multiples smaller than i * i have already been marked.
# for example 10, 15 20 , 25 , the 10, 15, 20 can coverd in iteration 2,3,5 so we can skip it


def primeOptimized(n):
    if n <= 2:
        return 0
    p = [True] * n
    p[0] = p[1] = False
    for i in range(2, int(n ** 0.5) + 1, 1):
        for j in range(i * i, n, i):
            p[j] = False
    print(sum(p))

primeOptimized(10)