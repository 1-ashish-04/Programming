# Hashmap variation : Frequency hashmap for String

s = "Ashish Jayaswal"

h = {}
count = 0
for i in s:
    if i in h:
        h[i] += 1
        # count = h[i]
        # count += 1
        # h[i] = count
    else:
        h[i] = 1

print(h)