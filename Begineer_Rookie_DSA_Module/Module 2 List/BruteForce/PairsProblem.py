# 5. we need to find pairs
# such that a[j]-a[i]==k 
# i<j
ar = [2,3,5,1,4]
k = 2
for i in range(len(ar)):
    for j in range(i+1, len(ar)):
        if(abs(ar[j] - ar[i]) == k):
            print(i,j, end=" | ")
    print()
