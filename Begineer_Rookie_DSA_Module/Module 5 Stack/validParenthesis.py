# Valid parenthesis

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

def validParenthesis(s):
    if len(s) > 0:
        l = [] # Stack
        for i in s:
            if i == "(" or i == "{"  or i == "[": # If only opening parenthesis then add to the last (top) of the stack
                l.append(i)
            # if current parenthesis is closing and last (top of) stack one also matching and length of stack is not equals to zero then pop it out
            elif len(l) !=0 and i == ")" and l[len(l)-1] == "(": 
                l.pop()
            elif len(l) !=0 and i == "}" and l[len(l)-1] == "{":
                l.pop()
            elif len(l) !=0 and i == "]" and l[len(l)-1] == "[":
                l.pop()
            else: # If having only closing parenthesis
                return False
    if len(l)!= 0: # If having only opening parenthesis
        return False
    return True

print(validParenthesis("(){{{{}}}"))