# print longest subarrays that
# have same starting and ending value  using list

a = [10,1,2,3,4,10,1,2,3,4,10,1,2,3,4]
h = {}
x = 0  # Track the index of the array

l = []  # Track the array
l2 = [] # Print the longest array

for i in a:
    if i not in h.keys(): # If value not present in hashmap
        h[i] = x # Insert the value as key  (First occcurence)
        # print(h)
        
    else:  # If value already present in hashmap
        
        start = h[i] # Accessing the first occurence index of that value
        # then printing the arr, which have first and last element is same

        for j in range(start, x+1):  # with x --> tracking the current position of same repeated value in arr
            # print(a[j], end=" ")
            l.append(a[j])
        # print()
        # print(len(l))
        if(len(l) > len(l2)):
            l2 = l
        l = []
        
    x += 1 # Iteration over the array, index based (0 indexing)
print(l2)
print("Length of the longest subarray", len(l2))
