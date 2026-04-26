# Remove duplicates from string

class RemoveDuplicates:

    def remove(self, text):
        s = set()
        s2 = ""
        for i in text:
            # if i in s:
            #     continue
            # else:
            #     s.add(i)
            #     s2 += i
            
            if i not in s:
                s.add(i)
                s2 += i


        print(s2)
        

r = RemoveDuplicates()

text = "aabcc"

r.remove(text)