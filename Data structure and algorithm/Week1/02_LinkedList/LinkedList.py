class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
    
    
    
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def print_list(self):
        print("[ ", end='')
        current = self.head
        while(current):
            print(current.data, end = ' , ' if current.next else '')
            current = current.next
        print(" ]")
        

def print_search_result(num, mylist):
    found = mylist.search(num)
    if found :
        print("{} found in my list".format(num))
    else:
        print("{} not found in my list".format(num))
     
if __name__ == '__main__':
            
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print("Number of elements in my list:" ,mylist.size())
    
    print_search_result(93,mylist)
    
    mylist.add(100)
    print_search_result(100, mylist)
    print("\n\n")

    print("Number of elements in my list after adding {}:".format(100) ,mylist.size())
    print("mylist after adding {} : ".format(100))
    mylist.print_list()

    print("\n\n")

    mylist.remove(54)
    print("Number of elements in my list after removing {}:".format(54) ,mylist.size())
    print("mylist after removing {} : ".format(54))
    mylist.print_list()

    print("\n\n")

    mylist.remove(93)
    print("Number of elements in my list after removing {}:".format(93) ,mylist.size())
    mylist.print_list()

    print("\n\n")
    
    mylist_reversed = mylist
    print("mylist Original : ")
    mylist_reversed.print_list()
    
    mylist_reversed.reverse()
    print("mylist reversed : ")
    mylist_reversed.print_list()