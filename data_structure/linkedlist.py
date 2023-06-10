class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None



class linkedlist:
    def __init__(self):
        self.head  = None

    def printLL(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


l1 =  linkedlist()
l1.head = node("mo")

l2 = node("tu")
l3 = node("wed")
l4 = node("thu")

l1.head.next = l2
l2.next = l3
l3.next = l4

print("helloooo")

l1.printLL()
