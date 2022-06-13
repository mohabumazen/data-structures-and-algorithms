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
        while current is not None:
            if current.value == x:
                return True

            current = current.next
        return False


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self, prev_node, value):
        if not prev_node:
            print("Previous node not in the list")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before_node(self, value, newVal):
        new_node = Node(newVal)
        current = self.head
        if current.value == value:
            new_node.next = current
            self.head = new_node
        else:
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

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
    llist.append(10)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.insert_after_node(llist.head.next, 77)
    print(llist.search(1))
    print(llist)

