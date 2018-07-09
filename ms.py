class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
    
    def Atending(self, data_in):
        NewNode = Node(data_in):
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode
        
    def Atafternode(self, middle_node, data_in):
        if middle_node is None:
            print("Don't have %s in this nodelist!" % middle_node)
            return 
        NewNode = Node(data_in)
        NewNode.next = middle_node.next
        middle_node.next = NewNode 
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next



