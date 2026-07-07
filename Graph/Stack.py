class Stack:

    def __init__(self, size):
      
        self.a = [0] * size
        self.top = -1

    def push(self, val): # insert value
        if self.top == len(self.a)-1:
            return "Stack is overflowed"
        self.top += 1
        self.a[self.top] = val
        return f"{val} inserted successfully in the stack"
    
    def pop(self): # remove peek (top) element
        if self.top == -1:
            return "Stack is underflow"
        val = self.a[self.top]
        self.a[self.top] = 0
        self.top -= 1
        return f"{val} Successfully removed."
    
    def top_value(self):
        if self.top == len(self.a)-1:
            return "Stack is empty"
        return f"Top value of stack is {self.a[self.top]}"
    
    def display(self):
        print(self.a)

s = Stack(4)

print(s.push(1))
print(s.push(2))
print(s.push(3))


print(s.top_value())

s.display()
print(s.pop())
s.display()

print(s.push(22))
print(s.push(33))

s.display()