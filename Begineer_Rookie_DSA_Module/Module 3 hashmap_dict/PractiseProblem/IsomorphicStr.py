# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# One-to-one mapping (injective + consistent mapping)
# No two characters in s map to the same character in t

# example 
# ada 
# bac
# a -- b
# d -- a   wrong

s = "egg"
t = "add"

def solution (s, t):
    # Step 1: Length check (isomorphic strings must be same length)
    if (len(s) != len(t)):
        return False
    h = {}  # Dictionary to store mapping from s → t
    x = 0  # Index pointer for string t

    for i in s:
        # Case 1: Character already mapped
        if i in h:
            # If mapped value does not match current t[x], invalid mapping
            if t[x] != h[i]: # Key present and value is not present
                return False 
            
        # Case 2: Character not mapped yet
        # But if t[x] is already mapped with some other character → invalid
        elif (t[x] in h.values() ): # key not present and value is present
            return False
        
        # Case 3: New valid mapping
        else:
            h[i] = t[x]

        # Move to next index in t
        x += 1
    
    # If all checks pass → strings are isomorphic
    return True

print(solution(s, t))
