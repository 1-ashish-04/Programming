s = ["h","e","l","l","o"]

i = 0
j = len(s) -1
while(i < j):
    c = s[i]
    s[i] = s[j]
    s[j] = c
    i += 1
    j -= 1

print(s)

