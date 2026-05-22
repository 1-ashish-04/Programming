class Solution:
    def removeDuplicate(sel, a):
        if len(a) == 0:
            return a
        # s = set()
        # s2 = ""
        # for i in a:
        #     if i not in s:
        #         s.add(i)
        #         s2 += i
        # return s2

        h = {}
        for i in a:
            if i in h:
                pass
            else:
                h[i] = 1
                print(i, end=" ")
      
            
        
            
s = Solution()
print(s.removeDuplicate("Ashish"))