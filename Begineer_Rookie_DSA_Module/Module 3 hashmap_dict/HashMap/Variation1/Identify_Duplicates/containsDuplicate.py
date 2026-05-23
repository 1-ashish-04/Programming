nums = [1,2,3,1,2]

def containDup(nums):
    h = {}
    for i in nums:
        if (i in h.keys()):
            return True
        else:
            h[i] = 0
    return False

    # Using set
    
    # s = set()
    #     for i in nums:
    #         if (i in s):
    #             return True
    #         else:
    #             s.add(i)
    #     return False

print(containDup(nums))