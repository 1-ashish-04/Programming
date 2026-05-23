# Count SubArr with unique element == K 
# Recheck not correct
class Solution:
    def subArrKUniqVal(self, n, k):
        h = {}
        i= 0
        j = 0
        count = 0
        while(i <= len(n)-1):
            if n[i]in h:
                h[n[i]] += 1
            else:
                h[n[i]] = 1
            if len(h) == k :
                count += 1
            elif len(h) > k:
                while(True):
                    if h[n[j]] == 1:
                        h.pop(n[j])
                        j += 1
                    elif h[n[j]] > 1:
                        h[n[j]] -= 1
                        count += 1
                        j += 1
                    if len(h) == k:
                        count += 1
                    elif len(h) < k:
                        break
            i += 1
   
        while(j <= len(n)-1):
            if h[n[j]] == 1:
                h.pop(n[j])
            elif h[n[j]] > 1:
                h[n[j]] -= 1
            if len(h) == k:
                count += 1
            j += 1
        return count
s = Solution()
print(s.subArrKUniqVal([1,1,2,3,4,5,5,5], 5))