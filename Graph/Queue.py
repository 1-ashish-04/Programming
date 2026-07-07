# Queue implementation
# Insert element from the starting of the list (at zero index)
# and remove the element from the end of the list (last index of the list)
q = []

q.insert(0,10)

q.insert(0,20)

print(q)
print("In reversed order queue", q[::-1])

q.pop()

print(q)