# Creating a single node that  will be present in the binary_tree
class tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def recursive_insert(self, value_insert):
        if value_insert < self.value:
            if self.left is None: # If the left node is not present...
                self.left = tree_node(value_insert) # ... creates the left node by storing the value passed in...
            else:
                # ... If the left node is present then this inserts the value passed in. Hence recursively calls recursive_insert on the left node.
                self.left.recursive_insert(value_insert) 
        else:
            if self.right is None: # Repeats the above statement on the right node
                self.right = tree_node(value_insert)
            else:
                self.right.recursive_insert(value_insert)

# Creating a brinary_tree class that represents the whole tree        
class binary_tree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value):
        if self.root is None:
            self.root = tree_node(value)
        else:
            self.root.recursive_insert(value) # Recursively searches the tree for an appropriate node to insert the passed value
            
    def print_from(self, starting_node):
        if starting_node.left is not None:
            self.print_from(starting_node.left) # Recursive insertion(recursively calls print_from on the child left node)
        print(starting_node.value)
        if starting_node.right is not None:
            self.print_from(starting_node.right) # Recursive insertion(recursively calls print_from on the child right node)

tree = binary_tree()

# Insert the value into the tree
tree.insert_node(29)
tree.insert_node(20)
tree.insert_node(17)
tree.insert_node(40)
tree.insert_node(25)
tree.insert_node(18)
tree.insert_node(1)

# Printing the whole tree.
tree.print_from(tree.root)