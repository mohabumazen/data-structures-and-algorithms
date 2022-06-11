from linked_list.linked_list import Node, LinkedList
import pytest

def test_node(node):
    assert node

def test_head_value(llist):
    actual = llist.head.value
    expected = 1

    assert actual == expected

def test_second_value(llist):
    actual = llist.head.next.value
    expected = 2

    assert actual == expected

def test_search(llist):
    actual = llist.search(1)
    expected = True

    assert actual == expected

def test_search_false(llist):
    actual = llist.search(55)
    expected = False

    assert actual == expected

def test_str(llist):
    actual = llist.__str__()
    expected = '< 1 > -> < 2 > -> < 3 > -> NULL'

    assert actual == expected



@pytest.fixture
def node():
    nod = Node()
    return nod

@pytest.fixture
def llist():
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.search(1)
    llist.search(55)
    return llist