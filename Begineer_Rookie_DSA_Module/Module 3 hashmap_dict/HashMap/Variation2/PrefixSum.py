# Variation 2 of hashMap


# HashMap variation 2:
# < index number, sum upto that index>


# Prefix sum

a  = [10,20,30,40,50,60,70]

h = {}
sum = 0

# for i in range( len(a)):
#         sum += a[i]
#         h[i+1] = sum

# print(h)

h = {}
x = 1
sum = 0
# 1 based indexing of hashMap  (Prefix sum)
for i in a:
        sum += i
        h[x] = sum
        x += 1

print(h)
