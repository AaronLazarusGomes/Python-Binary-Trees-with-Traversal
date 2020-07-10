#creating the Node class with left and right pointers
class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

#creating the BinaryTree class that will become the entire collection of Nodes
class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def preOrder(self, start):
        if(start):
            print(start.data)
            self.preOrder(start.left)
            self.preOrder(start.right)

    def inOrder(self, start):
        if(start):
            self.inOrder(start.left)
            print(start.data)
            self.inOrder(start.right)

    def postOrder(self, start):
        if(start):
            self.postOrder(start.left)
            self.postOrder(start.right)
            print(start.data)

    def addNode(self, node, val):
        if(node.data == None):
            node.data = Node(val)
            return
        else:
            if(node.data < val):
                if(node.right == None):
                    node.right = Node(val)
                else:
                    self.addNode(node.right, val)
            else:
                if(node.left == None):
                    node.left = Node(val)
                else:
                    self.addNode(node.left, val)


tree = BinaryTree(10)
tree.addNode(tree.root, 5)
tree.addNode(tree.root, 4)
tree.addNode(tree.root, 6)
tree.addNode(tree.root, 15)
tree.addNode(tree.root, 14)
tree.addNode(tree.root, 16)

tree.postOrder(tree.root)
tree.inOrder(tree.root)
tree.preOrder(tree.root)
