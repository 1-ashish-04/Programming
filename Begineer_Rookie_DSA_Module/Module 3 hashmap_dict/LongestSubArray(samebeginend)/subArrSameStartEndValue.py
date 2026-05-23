# print all the subarrays that
# have same starting and ending value

a = [10,1,2,3,4,10,1,2,3,4,10,1,2,3,4]
h = {}
x = 0  # Track the index of the array

for i in a:
    if i not in h.keys(): # If value not present in hashmap
        h[i] = x # Insert the value as key  (First occcurence)
        # print(h)
        
    else:  # If value already present in hashmap
        start = h[i] # Accessing the first occurence index of that value
        # then printing the arr, which have first and last element is same
        for j in range(start, x+1):  # with x --> tracking the current position of same repeated value in arr
            print(a[j], end=" ")
        print()
    x += 1 # Iteration over the array, index based (0 indexing)