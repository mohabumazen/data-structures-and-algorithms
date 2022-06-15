from linked_list.linked_list import LinkedList, Node
import pytest


def test_kth_element_out_of_linked(llist):
    actual = llist.find_Kth_from_End(6)
    expected = "Invalid Input, K is out of the linked-list"

    assert actual == expected


def test_kth_element_and_the_length_of_the_list_the_same(llist):
    actual = llist.find_Kth_from_End(5)
    expected = 12

    assert actual == expected


def test_kth_negative_integer(llist):

    actual = llist.find_Kth_from_End(-1)
    expected = "Invalid Input, K is negative number"

    assert actual == expected


def test_linked_list_of_size_one(llist2):
    actual = llist2.find_Kth_from_End(1)
    expected = 20

    assert actual == expected


def test_kth_not_in_the_end(llist):
    actual = llist.find_Kth_from_End(3)
    expected = 1

    assert actual == expected


@pytest.fixture
def node():
    nod = Node(value=5)
    return nod


@pytest.fixture
def llist():
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(7)
    llist.push(12)
    llist.search(1)
    llist.search(55)
    # llist.append(77)
    return llist


@pytest.fixture()
def llist2():
    llist2 = LinkedList()
    llist2.push(20)

    return llist2
