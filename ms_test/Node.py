class Node:     #构建单元结构
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:      #构建单链表
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):      #头部插入
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
    
    def Atending(self, data_in):        #尾部插入
        NewNode = Node(data_in)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode
        
    def Atafternode(self, middle_node, data_in):        #指定单元后方插入
        if middle_node is None:
            print("Don't have %s in this nodelist!" % middle_node)
            return 
        NewNode = Node(data_in)
        NewNode.next = middle_node.next
        middle_node.next = NewNode 
    
    def RemoveNode(self, Removekey):        #移除指定链表单元
        Heaval = self.head

        if Heaval:
            if Heaval == Removekey:
                self.head = Heaval.next                
                Heaval = None
                return
        while Heaval:
            if Heaval.data == Removekey:
                break
            prev = Heaval
            Heaval = Heaval.next
        if Heaval == None:
            return
        prev.next = Heaval.next
        Heaval = None

    def LListprint(self):       #顺序输出链表的单元 值
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next


