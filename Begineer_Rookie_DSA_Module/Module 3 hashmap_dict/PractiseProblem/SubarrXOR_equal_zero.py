# print ture if there exists a subarray whose xor=0
# else print false

a = [1,3,2,1,3,24]

# xor 
# 0 ^ 0 = 0
# 1 ^ 1 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1

def checkXorUsingHashmap(a):
    h = {} # hashmap
    xor = 0 # xor performed
    for i in a:
        xor ^= i  # xor operation
        if xor == 0 or xor in h.keys(): # check if it equals to zero or already in hashmap return true
            return True
        else: # else enter that element into the hashmap
            h[i] = 1
    return False

    # Dry run
    # [1,3,2,1,3,24]
    # 0 ^ 1 = 1 --> not equals t zero or in h --> insert it into h
    # 1 ^ 3 = 2 --> not equals t zero or in h --> insert it into h
    # 2 ^ 2 = 0 --> equals t zero return true --> [1,3,2] subarray whos xor is zero


print(checkXorUsingHashmap(a))

def xorUsingSet(a):
    s = set()
    xor = 0
    for i in a:
        xor ^= i
        if xor == 0 or xor in s:
            return True
        else:
            s.add(i)
    return False
