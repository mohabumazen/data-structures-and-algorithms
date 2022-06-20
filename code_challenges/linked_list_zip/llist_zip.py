from Data_Structures.Linked_list.linked_list import LinkedList


def zip_lists(llist_1, llist_2):

    current = llist_1.head
    current_second = llist_2.head

    counter = 0
    while current:
        counter += 1
        current = current.next
        if current is not None:
            break

    counter_second = 0
    while current_second:
        counter_second += 1
        current_second = current_second.next
        if current_second is None:
            break

    if counter < counter_second:
        head = llist_2.head.value
        current = llist_2.head
        current_second = llist_1.head

    elif counter_second <= counter:
        current = current.head
        current_second = current_second.head

    while current is not None or current_second is not None:

        if current_second is not None:
            new_next1 = current.next
            new_next2 = current_second.next
            current.next = current_second
            current = current.next
            if new_next1 is not None:
                current.next = new_next1
                current = current.next
            current_second = new_next2

        if current.next is None and current_second is None:
            current = current.next

        if current is None:
            if counter < counter_second:
                llist_1.push(head)

            return llist_1









