# Variation 1 in a hashMap

# frequency Array --> Number of times a element present in a list


a = [10,20,30,10,10,10,20,40,50,30,40,60,70,50,60,30,20,20,50]

h = {}

# {key, value } ---> {number, how many times of it occurence in a list}

for i in a:
    if(i in h.keys()):  # Number (key) already present in hashMap
        h[i] += 1 
        # count = h[i]
        # count += 1
        # h[i] = count
    else:               # Number (key) is not present
        h[i] = 1
    
print(h)