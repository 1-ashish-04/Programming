# creation
h = {}  # HAshMAp --> In python dict used as a hashMap

# Insertion 
h[1]="Pavan"
h[2] = "Prakash"

# Display 
print(h[1])
print(h[2])

# Update

h[2] = "Laptop"
print(h[2])

# Print all the keys of the hashMap
h[3] = "MAc"
h[12] = "Linux"

print(h.keys()) # dict_keys([1, 2, 3, 12])

# Print all the values of the hashMap

print(h.values()) # dict_values(['Pavan', 'Laptop', 'MAc', 'Linux'])

# Print complete hashmap
print(h)  # {1: 'Pavan', 2: 'Laptop', 3: 'MAc', 12: 'Linux'}

# Check if key present in hashMap or not
print(1 in h.keys()) # True

h["Ram"] = "Ayodhya"
print("Ram" in h.keys()) # True

# Check if value is present in hashMap
print("Pavan" in h.values())

#Iterating hashMap using for loop

for i in h.keys():
    print("Keys",i)
    print("Values", h[i])
    print("Key value pair", i, h[i])
