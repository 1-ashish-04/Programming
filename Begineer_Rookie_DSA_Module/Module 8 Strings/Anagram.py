class Anagram:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return True
        hs = {}
        ht = {}
        for i in range(len(s)):
            if s[i] in hs:
                hs[s[i]] += 1
            else:
                hs[s[i]] = 1
            if t[i] in ht:
                ht[t[i]] += 1
            else:
                ht[t[i]] = 1
        if len(hs) != len(ht):
            return False
        for i in hs:
            if i not in ht:
                return False
            elif hs[i] != ht[i]:
                return False
        return True


a = Anagram()

print(a.isAnagram("ate", "eat"))