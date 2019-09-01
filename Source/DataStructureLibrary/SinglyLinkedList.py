class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def isTail(self):
        return self.next is None

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, nodeValue):
        if self.isEmpty():
            self.head = node
            return

        lastNode = self.getTailNode()
        lastNode.next = Node(nodeValue)

    def getTailNode(self):
        if self.head is None:
            return None

        currNode = self.head
        while currNode.isTail() == False:
            currNode = currNode.next
        return currNode

    def insert(self, value, insertAt):
        if insertAt < 0 or insertAt >= self.getCount():
            print("ERROR: index to insert at is invalid")
            return

        if insertAt == 0:
            # insert at head
            newNode = Node(value, self.head)
            self.head = newNode
            return
        elif insertAt == self.getCount() - 1:
            # insert at end
            self.append(value)
            return

        # Insert somewhere...
        currIndex = 1
        previousNode = self.head
        currNode = self.head.next
        while currIndex != insertAt:
            # Goto the node to insert at
            previousNode = currNode
            currNode = currNode.next
            currIndex = currIndex + 1

        newNode = Node(value, currNode)
        previousNode.next = newNode

    def removeAtIndex(self, removeAt):
        if removeAt < 0 or removeAt >= self.getCount():
            print("ERROR: index to remove at is invalid")
            return

        if removeAt == 0:
            # Remove head
            self.head = self.head.next
            return

        currIndex = 1;
        beforeToRemoveNode = self.head
        while currIndex != removeAt:
            # goto node to remove at
            beforeToRemoveNode = beforeToRemoveNode.next
            currIndex = currIndex + 1

        print("Removed node's value: ", beforeToRemoveNode.next.value) # DEBUG!!!
        beforeToRemoveNode.next = beforeToRemoveNode.next.next

    def getCount(self):
        if self.isEmpty():
            return 0

        count = 1
        currNode = self.head
        while currNode.isTail() == False:
            currNode = currNode.next
            count = count + 1
        return count

    def reverse(self):
        if self.isEmpty():
            return
        currNode = self.head
        previousNode = None
        nextNode = None
        while not (currNode is None):
            nextNode = currNode.next
            currNode.next = previousNode
            previousNode = currNode
            currNode = nextNode
        self.head = previousNode

    def isEmpty(self):
        return self.head is None

    #Uses "tortoise and hare algorithm"
    def isLoop(self):
        if self.isEmpty():
            return False

        slowTraverser = self.head
        fastTraverser = self.head

        while True:
            slowTraverser = slowTraverser.next

            if fastTraverser.isTail():
                return False
            else:
                fastTraverser = fastTraverser.next.next

            if slowTraverser is None or fastTraverser is None:
                return False

            if slowTraverser == fastTraverser:
                return True

    def toList(self):
        if self.isEmpty():
            return []

        list = []
        currNode = self.head
        while currNode.isTail() == False:
            list.append(currNode.value)
            currNode = currNode.next
        return list

    def fromList(self, list):
        self.head = Node(list[0])
        currNode = self.head
        for index in range(1, len(list)):
            currNode.next = Node(list[index])
            currNode = currNode.next

    def display(self):
        if self.isEmpty():
            print("There is nothing inside this linked list!")

        toPrint = []
        currNode = self.head
        toPrint.append(str(currNode.value))
        while currNode.isTail() == False:
            currNode = currNode.next
            toPrint.append(" -> " + str(currNode.value))

        print(''.join(toPrint))
