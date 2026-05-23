# Stack

# data structure used --> List
# LIFO --> (Last In First Out)
# add into last --> append()
# remove from last --> pop()

x = 10
l = []
for i in range(1,10):
    if (i < 6):
        l.append(x)
        x += 10
    else:
        l.pop()
    print(l)


# [10]
# [10, 20]
# [10, 20, 30]
# [10, 20, 30, 40]
# [10, 20, 30, 40, 50]
# [10, 20, 30, 40]
# [10, 20, 30]
# [10, 20]
# [10]