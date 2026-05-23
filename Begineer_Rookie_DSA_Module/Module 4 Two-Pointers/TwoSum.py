# Two sum --> using Two Pointer, work only when the array is sorted
a = [2,4,7,8,60]
target = 9

result = [0,0]

i = 0
j = len(a) - 1

while(i < j):
    if a[i] +a[j] == target:
        result[0] = i 
        result[1] = j 
        break
    elif a[i] + a[j] > target:
        j -= 1
    else:
        i += 1

print(result)