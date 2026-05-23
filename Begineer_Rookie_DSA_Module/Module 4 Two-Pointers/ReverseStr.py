# Reverse the given string using the Two Pointer
s = ["h","e","l","l","o"]

i = 0 # Storing the left index
j = len(s) -1 # Storing the right index of the arr
while(i < j): # Use Two Pointer
    c = s[i] # Swap the element
    s[i] = s[j]
    s[j] = c
    i += 1
    j -= 1

print(s) # Print the result
