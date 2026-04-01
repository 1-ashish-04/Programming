class FindAllDuplicate:

    def find_all_dup(self, numms):

        # using set
        s = set()
        l = []
        for i in nums:
            if (i in s):
                l.append(i)
            else:
                s.add(i)
        print(l)
    
        # using hashmap
        
        # h = {}
        # l = []
        # for i in nums:
        #     if (i in h.keys()):
        #         l.append(i)
        #     else:
        #         h[i] = 0
        # print(l)
    
f = FindAllDuplicate()

nums = [4,3,2,7,8,2,3,1]

f.find_all_dup(nums)