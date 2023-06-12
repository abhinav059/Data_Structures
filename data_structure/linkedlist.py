class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None



class linkedlist:
    def __init__(self):
        self.head  = None

    def printLL(self):
        point = self.head
        while point is not None:
            print(point.data,"-->",end = " ")
            point = point.next

    def add_begin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    



# example to test the add_begin() function
# l1 = linkedlist()
# # l1.add_begin(10)
# # l1.add_end(90)
# # l1.add_begin(20)
# l1.add_end(100)

# l1.printLL()




# # the following lines are some examples to test the code.
# l1 =  linkedlist()
# l1.head = node("mo")

# l2 = node("tu")
# l3 = node("wed")
# l4 = node("thu")

# l1.head.next = l2
# l2.next = l3
# l3.next = l4

# print("helloooo")

# l1.printLL()
