class Solution:

    def compareStr(self, s,t):
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
    
s = Solution()
print(s.compareStr("Pavan","Pavan"))
    