# Group Anagrams

# Given an array of strings strs, group the together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

#     There is no string in strs that can be rearranged to form "bat".
#     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

def groupAnagrams(strs):
    h = {}
    for i in strs:
        temp = list(i) # convert one str into list
        temp.sort() # sort it
        temp = str(temp) # agrain convert to str --> to make key in hashmap
        if temp in h:
            h[temp].append(i) # if current str sorted order already present as key in hashmap, then append it
        else: 
            h[temp] = [i] # if comes first time then add it into the hashmap as list value into the sorted str val
    return list(h.values()) # all values of hashmap return as a list

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

def groupAnagrams2(strs):
    h = {}
    for i in strs:
        temp = "".join(sorted(i))
        if temp in h:
            h[temp].append(i)
        else:
            h[temp] = [i]
    return list(h.values())

print(groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))