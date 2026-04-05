# print longest subarrays that
# have same starting and ending value

a = [10,1,2,3,4,10,1,2,3,4,10,1,2,3,4]
a = [0,10,1,2,3,4,10,1,2,3,4,10,1,2,3,40,0,0,0,0,0,0,0,0,0,0,0]

h = {}
x = 0  # Track the index of the array

maxLen = 0 # Track the len of the array
mark1 = 0  # Starting index of the array
mark2 = 0  # last index of the array

for i in a:
    if i not in h:
        h[i] = x   # If value not present in the hashmap
        
    length =  x - h[i] + 1  # Length of the subarray --> End index - start index + 1 --> length of the array
    if i  in h.keys() and length > maxLen : # If value present and the maxlen is less  then current value
        maxLen = length
        mark1 = h[i]
        mark2 = x 
       
       
    x += 1 # Iteration over the array, index based (0 indexing)

for i in range(mark1, mark2+1 ): # Print the longest subarray where same starting and ending value
    print(a[i], end=" ")


print("\n length of the longest subarray", maxLen)