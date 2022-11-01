class stack:
    def __init__(self):
        self.internal_array = []

# Appending items into the array
    def push(self, data):
        self.internal_array.append(data)

# Popping(Deleting and returning the last item in the array)
    def pop(self):
        if len(self.internal_array) == 0:
            print("Stack is empty!")
        omega = self.internal_array[-1]
        del self.internal_array[-1]
        return omega

    def peek(self):
        self.internal_array[-1]
        return self.internal_array[-1]

# Defining how the class content is printed
    def __str__(self):
        return self.internal_array.__str__()

stack1 = stack()
stack1.push("January")
stack1.push("February")
stack1.push("March")
print(stack1)

stack2 = stack()
stack2.push("Linux")
stack2.push("Windows")
stack2.push("Mac OS X")
print(stack2)
print(" ")

popped1 = stack1.pop()
print(f"The popped off value is {popped1}")
popped2 = stack1.pop()
print(f"The popped off value is {popped2}")
print(" ")

popped1 = stack2.pop()
print(f"The popped off value is {popped1}")
popped2 = stack2.pop()
print(f"The popped off value is {popped2}")
print(" ")

peeked1 = stack1.peek()
print(f"The current top value is {peeked1}")
peeked2 = stack2.peek()
print(f"The current top value is {peeked2}")

