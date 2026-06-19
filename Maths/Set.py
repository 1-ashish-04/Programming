# Convert given two list into set and perform the union, intersection , a-b, b-a

# for that approach is  using hashmap
# mark element present only in a as 1
# only in b as 2
# and common in both as 3

a = [1,2,3,4,5,6,4,4,7,8,9]
b = [4,5,6,4,11,12,14,22]

h = {}
for i in a:
    h[i] = 1

for i in b:
    if i in h.keys() and h[i] == 1:
        h[i] = 3
    elif i not in h.keys():  # these needed to handle duplicate in b 
        h[i] = 2
# print(h)

# alternate way

h2 = {}
for i in a:
    h2[i] = 1

for i in b:
    if i in h2.keys():
        h2[i] = 3
    else:
        h2[i] = 2
# print(h2)

# Union of set
aUnionb = h.keys()
print("A UnionB ", aUnionb)

# A intersection B
print("A Intersection B")
for i in h:
    if h[i] == 3:
        print(i, end=" ")

print()

# A - B
# Element present in A, and not in B
print("A - B")
for i in h:
    if h[i] == 1:
        print(i, end=" ")

print()

# B - A
# Element present in B, and not in A
print("B - A")
for i in h:
    if h[i] == 2:
        print(i, end=" ")