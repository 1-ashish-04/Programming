# Find The Prefix Common Array OF Two Arrays

# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

# Example 1:

# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

# Example 2:

# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

class Solution:
    # def findThePrefixCommonArray(self, A, B):
    #     hA = {}
    #     hB = {}
    #     c = []
    #     count = 0
    #     for i in range(len(A)):
    #         hA[i] = A[i]
    #         hB[i] = B[i]
    #         if hA[i] in hB.values():
    #             count += 1
    #         if hB[i] in hA.values() and hA[i] != hB[i]:
    #             count += 1
    #         c.append(count)
    #     return c

    def findThePrefixCommonArray(self, A, B):
        sA = set()
        sB = set()
        c = []
        count = 0
        for i in range(len(A)):
            sA.add(A[i])
            sB.add(B[i])
            if A[i] in sB:
                count += 1
            if B[i] in sA and A[i] != B[i]:
                count += 1
            c.append(count)
        return c

s = Solution()
print(s.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))