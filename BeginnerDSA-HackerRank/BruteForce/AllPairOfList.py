# Brute Force
ar = [1,2,3,4,5]

# Approach one 

# consider all the pairs  (With repeatation)
for i in ar:
    for j in ar:
        print( i,j, end=" | ")
    print("")

# Approach two 

# when i<j (Without repeatation) 
# i start from 0  and   j start from j = i + 1
print("i < j")
for i in range(len(ar)):
    for j in range(i+1, len(ar)):
        print(ar[i],ar[j], end=" | ")
    print("")


# 1. Print all the sum of pairs

for i in ar:
    for j in ar:
        print(i,'+',j,'-->', i+j, end=" | ")
    print()

# 2. print pairs sums with i<j , two different numbers
print(" ")
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        print(ar[i],'+',ar[j],'-->', ar[i]+ar[j], end=" | ")
    print()


# 3. print all the pairs (i,j) where sum=k and i<j
# Two sum
sum = 7
l = []
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        if(ar[i]+ar[j] == sum):
            print(ar[i],ar[j])

            l.append(ar[i]+ar[j])
            l.append(i)
            l.append(j)
            l.append("value")
print(l)


#  4. Triplet sum
# u need to find a[i]+a[j]+a[k] == sum
# and i<j<k


for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        for k in range(j+1,len(ar)):
            print(ar[i]+ar[j]+ar[k],end=" | ")
        print("")

# 5. we need to find pairs
# such that a[j]-a[i]==k 
# i<j

k = 2
for i in range(len(ar)):
    for j in range(i+1, len(ar)):
        if(ar[j] - ar[i] == k): # works only when there is a sorted list, for un sorted list need to use a abs() method.
            print(ar[j], ar[i], end=" | ")
    print()
