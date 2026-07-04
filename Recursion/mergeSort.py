def merge(a,l, mid, r):
    i = l # upto mid
    j = mid+1 # upto r
    c = []
    while(i<= mid and j<= r):
        if a[i] <= a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    while(i<= mid):
        c.append(a[i])
        i += 1
    while(j <= r):
        c.append(a[j])
        j += 1
    k = 0
    for i in range(l,r+1,1):
        a[i] = c[k]
        k += 1

def mergeSort(a, l, r):
    if l < r:
        mid = (l+r)//2
        mergeSort(a, l, mid)
        mergeSort(a, mid+1, r)
        merge(a, l, mid, r)

a = [38,9,34,43,10,12,6]
mergeSort(a, 0, len(a)-1)
print(a)