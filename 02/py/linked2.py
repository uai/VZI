# double linked list + iterator


class Node:
    def __init__(self, data_):
        self.data = data_
        self.next = None
        self.pred = None

    def getData(self):
        return self.data

    def setNext(self, newNext):
        self.next = newNext

    def setPred(self, newPred):
        self.pred = newPred

    def getNext(self):
        return self.next

    def getPred(self):
        return self.pred

#------------------------------------------------
class ListIterator(object):
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()

        result = self.current.data
        self.current = self.current.next

        return result

#------------------------------------------------
class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __iter__(self):
        return ListIterator(self.head)

    def isEmpty(self):
        return self.head == None

    def pushBack(self, item):
        temp = Node(item)
        self.size += 1

        if self.isEmpty():
            self.head = temp
            self.last = self.head
        else:
            self.last.setNext(temp)
            temp.setPred(self.last)
            temp.setNext(None)
            self.last = temp

    def printList(self):
        current = self.head

        while(current is not None):
            print(current.getData())
            current = current.getNext()

    def remove(self, data):

        current = self.head
        while current != None:
            if current.data == data:

                if current.pred!= None:
                    current.pred.next = current.next
                else:
                    self.head = current.next

                if current.next != None:
                    current.next.pred = current.pred
                else:
                    self.last = current.pred

                self.size -= 1

            current = current.next

# main()
#--------------------------------------

lst = DoubleLinkedList()

lst.pushBack(1)
lst.pushBack(2)
lst.pushBack(3)

# using iterator
for data in lst:
    print(data)

print("-----------")

# lst.remove(2)
# lst.remove(1)
lst.remove(3)

for data in lst:
    print(data)

