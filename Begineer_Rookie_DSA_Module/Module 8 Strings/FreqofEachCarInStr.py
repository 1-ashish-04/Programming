class Solution:

    def freqOfStr(self, s):
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        return h

s = Solution()

print(s.freqOfStr("Ashish Jayaswal"))