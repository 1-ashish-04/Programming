# Merge String Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class MergeStrAlternate:
    def solution(self, word1, word2):
        m = min(len(word1), len(word2))
        mStr = ""

        for i in range(m):
            mStr += word1[i] + word2[i]

        if (len(word1) > m):
            for i in range(m, len(word1)):
                mStr += word1[i]

        elif (len(word2) > m):
            for i in range(m, len(word2)):
                mStr += word2[i]
        
        return mStr

m = MergeStrAlternate()

result = m.solution("abc", "pqr")
print(result)

result = m.solution("ab", "pqrs")
print(result)

result = m.solution("abcdef", "pqr")
print(result)