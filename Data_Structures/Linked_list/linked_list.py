class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        """
        Takes a value and pushes this value in a new node at the first of the linked-list

        :param value: int, str
        :return: a new node at the first of the linked list with the given value.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        """
        Takes a value to search for in the linked-list

        :param x: int, str
        :return: A boolean value (True or False)
        """
        current = self.head
        while current is not None:
            if current.value == x:
                return True

            current = current.next
        return False


    def append(self, value):
        """
        Takes a value and add a new node with the given value to the end of the linked-list.

        :param value: int, str
        :return: A new node with the given value
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self, prev_node, value):
        """
        Add a new node with a given value after a specific node.

        :param prev_node:
        :param value: int, str
        :return: A new node after the specified node.
        """
        if not prev_node:
            print("Previous node not in the list")
            return
        curr = self.head
        while curr:
            if curr.value == prev_node:
                break
            curr = curr.next

        prev_node = curr
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before_node(self, value, newVal):
        """
        Add a new node with a given value before a specific value.

        :param value:
        :param newVal: int, str
        :return: A new node before the specified node.
        """
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

    def find_Kth_from_End(self, k):
        """
        A function to find a specific node, (Kth node starting from the end of the linked-list).

        :param k: The index of the specified node
        :return: The value of the specified node.
        """
        if k < 0:
            return "Invalid Input, K is negative number"
        current = self.head
        second_current = self.head

        count = 0

        while second_current:
            count += 1
            if k == count:
                break
            second_current = second_current.next
            if not second_current:
                return "Invalid Input, K is out of the linked-list"

        while second_current.next:
            second_current = second_current.next
            current = current.next
        return current.value

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
    print(llist.find_Kth_from_End(6))
    print(llist)
