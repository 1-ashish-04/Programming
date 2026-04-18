# Unique Number of Occurences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

def uniqueOccurrences(arr):
    h = {} # Store the frequency of the array 
    for i in arr:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
    # print (h)  # -->   {1: 3, 2: 2, 3: 1}
    # Usinq set validate unique nummber of occurences
    s = set()
    for i in h:
        if h[i] in s: # if h.values() already present in the s , means repeated occurences, return False
            return False
        s.add(h[i]) # else add it into the set, if first time coming.
    return True

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))