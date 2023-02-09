class MyLinkedList:
    """
    Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
    A node in a singly linked list should have two attributes: val and next. val is the value of the current node, 
        and next is a pointer/reference to the next node.
    If you want to use the doubly linked list, you will need one more attribute prev 
    to indicate the previous node in the linked list. 
    Assume all nodes in the linked list are 0-indexed.

    Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
        If index equals the length of the linked list, the node will be appended to the end of the linked list. 
        If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
    """

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        currentNode = self.head.next
        while currentNode and index > 0:
            currentNode = currentNode.next
            index -= 1
        if currentNode and currentNode != self.tail and index == 0:
            return currentNode.val
        return -1

    def addAtHead(self, val: int) -> None:
        # define newNode, 
        # next (node that would be next value for this new node), 
        # prev (node that would be prev value for this new node)
        newNode, next, prev = ListNode(val), self.head.next, self.head

        # updating prev(dummyHead) and next(currentHead) to point to newNode 
        prev.next = newNode
        next.prev = newNode
        
        # updating newNode to point to prev(dummyHead) and next(currentHead)
        newNode.next = next
        newNode.prev = prev
        
        
    def addAtTail(self, val: int) -> None:
        # define newNode, 
        # next (node that would be next value for this new node), 
        # prev (node that would be prev value for this new node)
        newNode, next, prev = ListNode(val), self.tail, self.tail.prev

        # updating prev(currentTail) and next(dummyTail) to point to newNode 
        prev.next = newNode
        next.prev = newNode
        
        # updating newNode to point to prev(currentTail) and next(dummyTail)
        newNode.next = next
        newNode.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        # get prev and next for node to be added
        # We are going to implement the get function but instead 
        # of returning values we will be returning the pointer for node
        currentNode = self.head.next
        while currentNode and index > 0:
            currentNode = currentNode.next
            index -= 1
        if currentNode and index == 0:
            # in this case next is going to be the current as we will be adding
            # the new node between the current node and the current.prev node
            newNode, prev, next = ListNode(val), currentNode.prev, currentNode
            # updating prev and next to point to newNode 
            prev.next = newNode
            next.prev = newNode
        
            # updating newNode to point to prev and next
            newNode.next = next
            newNode.prev = prev
            
    def deleteAtIndex(self, index: int) -> None:
        # get prev and next for node to be deleted
        # We are going to implement the get function but instead 
        # of returning values we will be returning the pointer for node
        currentNode = self.head.next
        while currentNode and index > 0:
            currentNode = currentNode.next
            index -= 1
        if currentNode and index == 0 and currentNode != self.tail:
            # in this case next is going to be the current.next as we will be 
            # adding the new node between the current node and the 
            # current.prev node
            prev, next = currentNode.prev, currentNode.next
            # to delete a node we need to connect the prev node to next node 
            prev.next = next
            next.prev = prev

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)