# Two Sum

a = [2,3,4,5,20]
target = 23
h = {}
x = 0
for i in a:
    if ((target - i ) in h.keys()):
        print([ h[target - i], x])
        break
    h[i] = x
    x+= 1