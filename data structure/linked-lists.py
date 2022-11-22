
class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def link(self, new_node):
        self.next = new_node
        new_node.prev = self

    def __str__(self):
        return self.data

class linked_list:
    def __init__(self):
        self.first = None
        self.last = None

# Implementing a add() method to add new nodes to the last self.last node.
    def add(self, new_node):
        if self.first is None:
            self.first = new_node
        else:
            self.last.link(new_node)
        self.last = new_node

    def get(self, index):
        count = 0
        current_node = self.first
        while count < index:
            count += 1
            current_node = current_node.next
        return current_node
        


node1 = node("Apple")
node2 = node("Banana")

print(node1)
print(node2)

print("Linking two nodes..")
node1.link(node2)

print("Testing link()... prev and next for node1")
print(node1.prev)
print(node1.next)

print("Testing link()... prev and next for node2")
print(node2.prev)
print(node2.next)

