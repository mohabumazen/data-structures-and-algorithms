from Data_Structures.Linked_list.linked_list import Node, LinkedList
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

def test_append(llist):
    llist.append(77)

    assert str(llist) == f'< {1} > -> < {2} > -> < {3} > -> < {77} > -> NULL'

def test_insert_after_node(llist):
    llist.insert_after_node(3, 4)
    assert str(llist) == f'< {1} > -> < {2} > -> < {3} > -> < {4} > -> NULL'

def test_insert_before_node(llist):
    llist.insert_before_node(2, 8)
    assert str(llist) == f'< {1} > -> < {8} > -> < {2} > -> < {3} > -> NULL'

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
    llist.search(1)
    llist.search(55)
    # llist.append(77)
    return llist