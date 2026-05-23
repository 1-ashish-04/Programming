a = []  # list
print(a)

# append ----> used to insert element from the last of list , single element at a time
a.append(10)
a.append("Ashish")
a.append(2.2)
a.append(2)
print(a)

print(a[1]) # accessing the specific index value
a[2]= 4.4
print(a)

a.pop()  # removing element with pop , if no index is passed then last element will get remove, if index pass then specific value remove
print(a)

print(a.pop(1))
print(a)


a=[]
a.append(10)
a.append(20)
a.append(430)
a.append(71)
print(a)

x=min(a) # minimum value from the list
y=max(a) # maximum value from the list
print(x)
print(y)

# in ---> used to check specific element present in list or not, if yes then return True, otherwise False
print(10 in a) 
print(200 in a)

# sort() ---> used to sort the list into the ascending / increasing order
print(a)
a.sort()
print(a)

# to make decreasing order sort --> first use sort() method then use list slicing a[:: -1] which make the list reverse
print(a[::-1])

