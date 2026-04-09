class ValidAnagram:
    def solution(self, s, t):
        if (len(s) != len(t)):
            return False
        s1 = {}
        t1 = {}
        for i in range(len(s)):
            if s[i] in s1.keys():
                s1[s[i]] +=1
            else:
                s1[s[i]] = 1

            if t[i] in t1.keys():
                t1[t[i]] += 1
            else:
                t1[t[i]] = 1
        
        if(len(s1) != len(t1)):
            return False
        
        for i in s1.keys():
            if i not in t1.keys():
                return False
            if s1[i] != t1[i]:
                return False
        return True
    
    def solution2(self, s , t):
        if(len(s) != len(t)):
            return False
        
        s1 = {}
        t1 = {}
        for i in s:
            if i in s1.keys():
                s1[i] += 1
            else:
                s1[i] = 1
        for i in t:
            if i in t1.keys():
                t1[i] += 1
            else:
                t1[i] = 1
        
        if(len(s1 ) != len(t1)):
            return False
        
        for i in s1.keys():
            if i not in t1.keys():
                return False
            elif s1[i] != t1[i]:
                return False
        return True
    
vA = ValidAnagram()

check = vA.solution("rccecar", "carrace")
print(check)

