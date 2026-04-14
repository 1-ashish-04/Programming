# First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class FirstUniqueCharInStr:
    def solution(Self, s):
        h = {} # hashmap to store the frequency of the char
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        x = 0 # Iterate the index
        for i in s:
            if h[i] == 1: # check the first presence of an element
                return x # return index of that char
            x += 1
        return -1 # if no such index then return the -1

f = FirstUniqueCharInStr()

result = f.solution("leetcode")
print(result)

result = f.solution("aabb")
print(result)