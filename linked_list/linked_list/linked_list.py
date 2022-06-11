class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, x):
        current = self.head
        while current != None:
            if current.value == x:
                return True 
            
            current = current.next
        return False

    def __str__(self):
        current = self.head
        items = ''
        while current:
            items += f'< {current.value} > -> '
            current = current.next
        items += "NULL"
        return items
    
if __name__ == '__main__':

    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print(llist.search(1))
    print(llist)

