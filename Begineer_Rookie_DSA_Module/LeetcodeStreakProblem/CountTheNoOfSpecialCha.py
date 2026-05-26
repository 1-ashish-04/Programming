# Count The Number Of Special Characters I

# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

# Return the number of special letters in word.

# Example 1:

# Input: word = "aaAbcBC"

# Output: 3

# Explanation:

# The special characters in word are 'a', 'b', and 'c'.

# Example 2:

# Input: word = "abc"

# Output: 0

# Explanation:

# No character in word appears in uppercase.

class Solution:
    def numberOfSpecialChars(self, word):
        w = ""
        s = set()
        for i in word:
            if i not in s:
                w += i
                s.add(i)
        count = 0
        h = {}
        for i in w:
            if i.lower() in h and h[i.lower()] == 1:
                h[i.lower()] += 1
                count += 1
            elif i.upper() in h and h[ i.upper()] == 1:
                h[ i.upper()] += 1
                count += 1
            else:
                h[i] = 1
        return count
    
    def numberOfSpecialChars2(self, word):
        lowS = set()
        uppS = set()
        for i in word:
            if i.isupper():
                uppS.add(i.lower())
            elif i.islower():
                lowS.add(i)
        return len(lowS and uppS)
s = Solution()

print(s.numberOfSpecialChars("aaAbcBC"))
print(s.numberOfSpecialChars2("aaAbcBC"))